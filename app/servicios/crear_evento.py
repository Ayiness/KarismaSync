import sqlite3
from dataclasses import dataclass, field
from datetime import date, datetime, timezone

from app.dominio import asistencia as ciclo_asistencia
from app.dominio.evento_ensayo import EventoDeEnsayo, transicionar
from app.integraciones.notificaciones import (
    RespuestaEnvio,
    ServicioNotificaciones,
    obtener_servicio_notificaciones,
)


class ErrorCreacionEvento(ValueError):
    pass


@dataclass
class Convocado:
    integrante_id: int
    instrumentos_ids: list[int] = field(default_factory=list)


@dataclass
class DatosNuevoEvento:
    fecha: str
    quorum: str | int | None
    convocados: list[Convocado] = field(default_factory=list)
    canciones_ids: list[int] = field(default_factory=list)


@dataclass
class ResultadoCreacion:
    evento_id: int
    destinatarios: int
    respuesta_envio: RespuestaEnvio


def crear_evento(
    conexion: sqlite3.Connection,
    usuario_id: int,
    datos: DatosNuevoEvento,
    servicio_notificaciones: ServicioNotificaciones | None = None,
) -> ResultadoCreacion:
    usuario = conexion.execute(
        "SELECT * FROM integrantes WHERE id = ?", (usuario_id,)
    ).fetchone()
    if usuario is None:
        raise ErrorCreacionEvento("seleccione un usuario de demostración")
    if not usuario["es_lider"]:
        raise ErrorCreacionEvento(
            "solo el Líder de Alabanza puede crear eventos de ensayo"
        )

    integrantes_banda = {
        fila["id"]
        for fila in conexion.execute(
            "SELECT id FROM integrantes WHERE banda_id = ?", (usuario["banda_id"],)
        )
    }

    convocados: dict[int, list[int]] = {}
    for convocado in datos.convocados:
        try:
            integrante_id = int(convocado.integrante_id)
            instrumentos_ids = sorted({int(valor) for valor in convocado.instrumentos_ids})
        except (TypeError, ValueError) as error:
            raise ErrorCreacionEvento(
                "cada músico convocado debe tener al menos un instrumento"
            ) from error
        if integrante_id not in integrantes_banda:
            raise ErrorCreacionEvento("solo puede convocar integrantes de su banda")
        if not instrumentos_ids:
            raise ErrorCreacionEvento(
                "cada músico convocado debe tener al menos un instrumento"
            )
        convocados[integrante_id] = instrumentos_ids

    if not convocados:
        raise ErrorCreacionEvento("debe convocar al menos un músico")

    instrumentos_del_evento = sorted(
        {instrumento for lista in convocados.values() for instrumento in lista}
    )
    marcadores = ", ".join("?" for _ in instrumentos_del_evento)
    existentes = {
        fila["id"]
        for fila in conexion.execute(
            f"SELECT id FROM instrumentos WHERE id IN ({marcadores})",
            instrumentos_del_evento,
        )
    }
    if existentes != set(instrumentos_del_evento):
        raise ErrorCreacionEvento(
            "cada músico convocado debe tener al menos un instrumento válido"
        )

    quorum_ingresado = "" if datos.quorum is None else str(datos.quorum).strip()
    try:
        quorum = int(quorum_ingresado)
    except ValueError:
        quorum = None
    if quorum is None or quorum < 1:
        raise ErrorCreacionEvento("debe indicar el quórum requerido")
    if quorum > len(convocados):
        raise ErrorCreacionEvento(
            "el quórum no puede superar la cantidad de músicos convocados"
        )

    fecha_ingresada = str(datos.fecha or "").strip()
    try:
        fecha_iso = date.fromisoformat(fecha_ingresada).isoformat()
    except ValueError as error:
        raise ErrorCreacionEvento("debe indicar una fecha válida") from error

    try:
        canciones_ids = sorted({int(valor) for valor in datos.canciones_ids})
    except (TypeError, ValueError) as error:
        raise ErrorCreacionEvento(
            "seleccione canciones válidas del catálogo"
        ) from error

    if canciones_ids:
        marcadores_canciones = ", ".join("?" for _ in canciones_ids)
        canciones_existentes = {
            fila["id"]
            for fila in conexion.execute(
                f"SELECT id FROM canciones WHERE id IN ({marcadores_canciones})",
                canciones_ids,
            )
        }
        if canciones_existentes != set(canciones_ids):
            raise ErrorCreacionEvento("seleccione canciones válidas del catálogo")

    servicio = servicio_notificaciones or obtener_servicio_notificaciones(conexion)

    try:
        evento = EventoDeEnsayo(
            banda_id=usuario["banda_id"],
            fecha=fecha_iso,
            quorum=quorum,
        )
        transicionar(evento, "crearEvento")

        cursor = conexion.execute(
            "INSERT INTO eventos_ensayo (banda_id, fecha, quorum, estado) "
            "VALUES (?, ?, ?, ?)",
            (evento.banda_id, evento.fecha, evento.quorum, evento.estado),
        )
        evento_id = cursor.lastrowid

        for cancion_id in canciones_ids:
            conexion.execute(
                "INSERT INTO eventos_canciones (evento_id, cancion_id) VALUES (?, ?)",
                (evento_id, cancion_id),
            )

        fecha_envio = datetime.now(timezone.utc).isoformat(timespec="seconds")
        for integrante_id, instrumentos_ids in sorted(convocados.items()):
            cursor = conexion.execute(
                "INSERT INTO convocatorias "
                "(evento_id, integrante_id, fecha_ensayo, fecha_envio) "
                "VALUES (?, ?, ?, ?)",
                (evento_id, integrante_id, evento.fecha, fecha_envio),
            )
            convocatoria_id = cursor.lastrowid
            conexion.execute(
                "INSERT INTO asistencias (convocatoria_id, estado) VALUES (?, ?)",
                (
                    convocatoria_id,
                    ciclo_asistencia.transicionar(
                        ciclo_asistencia.ESTADO_INICIAL, "convocatoriaEmitida"
                    ),
                ),
            )
            for instrumento_id in instrumentos_ids:
                conexion.execute(
                    "INSERT INTO convocatorias_instrumentos "
                    "(convocatoria_id, instrumento_id) VALUES (?, ?)",
                    (convocatoria_id, instrumento_id),
                )

        for instrumento_id in instrumentos_del_evento:
            conexion.execute(
                "INSERT INTO eventos_requieren_instrumentos (evento_id, instrumento_id) "
                "VALUES (?, ?)",
                (evento_id, instrumento_id),
            )

        marcadores_convocados = ", ".join("?" for _ in convocados)
        destinatarios = conexion.execute(
            f"SELECT id, nombre FROM integrantes WHERE id IN ({marcadores_convocados}) "
            "ORDER BY id",
            tuple(convocados),
        ).fetchall()

        respuesta = servicio.enviar_convocatoria(
            destinatarios,
            {
                "id": evento_id,
                "banda_id": evento.banda_id,
                "fecha": evento.fecha,
                "estado": evento.estado,
            },
            f"/eventos/{evento_id}",
        )
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise

    return ResultadoCreacion(
        evento_id=evento_id,
        destinatarios=len(destinatarios),
        respuesta_envio=respuesta,
    )
