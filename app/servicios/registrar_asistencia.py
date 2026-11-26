"""Responder la convocatoria de un evento (HU-03, CU-05, DSS-05)."""

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone

from app.dominio.asistencia import EstadoAsistencia, transicionar
from app.dominio.evento_ensayo import ErrorTransicion, EstadoEvento

LARGO_MAXIMO_MOTIVO = 200


class ErrorRespuesta(ValueError):
    """respuestaRechazada(motivo) de DSS-05."""

    def __init__(self, mensaje: str, motivo: str):
        super().__init__(mensaje)
        self.motivo = motivo


class EventoNoEncontrado(LookupError):
    pass


@dataclass
class ResultadoRespuesta:
    """respuestaRegistrada(evento, estadoAsistencia) de DSS-05."""

    evento_id: int
    estado: str


def registrar_asistencia(
    conexion: sqlite3.Connection,
    usuario_id: int | None,
    evento_id: int,
    asiste: bool,
    motivo: str | None = None,
    instrumentos_ids: list[int] | None = None,
) -> ResultadoRespuesta:
    if usuario_id is None:
        raise ErrorRespuesta("seleccione un usuario de demostración", "sinUsuario")

    evento = conexion.execute(
        "SELECT id, estado FROM eventos_ensayo WHERE id = ?", (evento_id,)
    ).fetchone()
    if evento is None:
        raise EventoNoEncontrado(evento_id)

    fila = conexion.execute(
        "SELECT a.id, a.estado FROM convocatorias c "
        "LEFT JOIN asistencias a ON a.convocatoria_id = c.id "
        "WHERE c.evento_id = ? AND c.integrante_id = ?",
        (evento_id, usuario_id),
    ).fetchone()
    if fila is None:
        raise ErrorRespuesta("no fuiste convocado a este evento", "noConvocado")

    # Un evento masivo sin aprobar no tiene asistencias: no se puede responder.
    if evento["estado"] != EstadoEvento.VIGENTE.value or fila["id"] is None:
        raise ErrorRespuesta(
            "la convocatoria ya no está disponible", "convocatoriaNoDisponible"
        )

    if instrumentos_ids:
        raise ErrorRespuesta(
            "solo el Líder de Alabanza puede asignar los instrumentos",
            "instrumentosAsignadosPorLider",
        )

    motivo_limpio = (motivo or "").strip()
    if not asiste:
        if not motivo_limpio:
            raise ErrorRespuesta(
                "debe indicar el motivo por el que no asistirá", "sinMotivo"
            )
        if len(motivo_limpio) > LARGO_MAXIMO_MOTIVO:
            raise ErrorRespuesta(
                f"el motivo no puede superar los {LARGO_MAXIMO_MOTIVO} caracteres",
                "sinMotivo",
            )

    try:
        nuevo_estado = transicionar(fila["estado"], "registrarAsistencia", asiste)
    except ErrorTransicion as error:
        raise ErrorRespuesta(str(error), "transicionNoPermitida") from error

    conexion.execute(
        "UPDATE asistencias SET estado = ?, motivo = ?, fecha_respuesta = ? WHERE id = ?",
        (
            nuevo_estado,
            motivo_limpio if nuevo_estado == EstadoAsistencia.NO_ASISTE.value else None,
            datetime.now(timezone.utc).isoformat(timespec="seconds"),
            fila["id"],
        ),
    )
    conexion.commit()
    return ResultadoRespuesta(evento_id=evento_id, estado=nuevo_estado)
