"""Revisar la convocatoria de un evento masivo (HU-08, CU-07, DSS-07)."""

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum

from app.dominio.evento_ensayo import (
    ErrorTransicion,
    EstadoEvento,
    TipoEvento,
    transicionar,
)
from app.dominio.integrante import RolIntegrante, es_representante
from app.integraciones.notificaciones import (
    ServicioNotificaciones,
    obtener_servicio_notificaciones,
)
from app.servicios.crear_evento import emitir_convocatorias
from app.servicios.registrar_asistencia import EventoNoEncontrado

LARGO_MAXIMO_JUSTIFICACION = 200


class DecisionRevision(str, Enum):
    APROBADA = "Aprobada"
    RECHAZADA = "Rechazada"


class ErrorRevision(ValueError):
    """revisionRechazada(motivo) de DSS-07."""

    def __init__(self, mensaje: str, motivo: str):
        super().__init__(mensaje)
        self.motivo = motivo


@dataclass
class ResultadoRevision:
    """revisionRegistrada(evento, decision) de DSS-07."""

    evento_id: int
    decision: str
    estado: str


def eventos_por_revisar(
    conexion: sqlite3.Connection, usuario: sqlite3.Row | None
) -> list[sqlite3.Row]:
    """verEventosPorRevisar() -> eventosPendientes(eventos) de DSS-07 (HU-08 CA1)."""
    if not es_representante(usuario):
        return []
    return conexion.execute(
        "SELECT e.id, e.fecha, e.quorum, e.tipo, e.estado, "
        "  (SELECT COUNT(*) FROM convocatorias c WHERE c.evento_id = e.id) "
        "   AS total_convocatorias "
        "FROM eventos_ensayo e "
        "WHERE e.banda_id = ? AND e.tipo = ? AND e.estado = ? "
        "ORDER BY e.fecha, e.id",
        (
            usuario["banda_id"],
            TipoEvento.MASIVO.value,
            EstadoEvento.PENDIENTE_APROBACION.value,
        ),
    ).fetchall()


def resolver_revision(
    conexion: sqlite3.Connection,
    usuario_id: int | None,
    evento_id: int,
    decision: str,
    justificacion: str | None = None,
    servicio_notificaciones: ServicioNotificaciones | None = None,
) -> ResultadoRevision:
    """resolverRevision(evento, decision, justificacion) de DSS-07."""
    usuario = None
    if usuario_id is not None:
        usuario = conexion.execute(
            "SELECT * FROM integrantes WHERE id = ?", (usuario_id,)
        ).fetchone()

    evento = conexion.execute(
        "SELECT * FROM eventos_ensayo WHERE id = ?", (evento_id,)
    ).fetchone()
    if evento is None:
        raise EventoNoEncontrado(evento_id)

    # RNF-01 / HU-08 CA7-CA8: solo el Representante de músicos de la banda revisa.
    if not es_representante(usuario) or usuario["banda_id"] != evento["banda_id"]:
        raise ErrorRevision(
            "solo el Representante de músicos de la banda puede revisar "
            "eventos masivos",
            "sinPermiso",
        )

    # HU-08 CA6: solo eventos masivos pendientes de aprobación.
    if (
        evento["tipo"] != TipoEvento.MASIVO.value
        or evento["estado"] != EstadoEvento.PENDIENTE_APROBACION.value
    ):
        raise ErrorRevision("el evento ya fue revisado o no es masivo", "eventoNoRevisable")

    if decision not in {d.value for d in DecisionRevision}:
        raise ErrorRevision("seleccione aprobar o rechazar", "decisionInvalida")

    justificacion_limpia = (justificacion or "").strip()
    if decision == DecisionRevision.RECHAZADA.value:
        # HU-08 CA4-CA5: la justificación es obligatoria al rechazar.
        if not justificacion_limpia:
            raise ErrorRevision(
                "debe indicar la justificación del rechazo", "sinJustificacion"
            )
        if len(justificacion_limpia) > LARGO_MAXIMO_JUSTIFICACION:
            raise ErrorRevision(
                f"la justificación no puede superar los "
                f"{LARGO_MAXIMO_JUSTIFICACION} caracteres",
                "sinJustificacion",
            )
    else:
        justificacion_limpia = ""

    evento_estado = (
        "aprobarEvento" if decision == DecisionRevision.APROBADA.value else "rechazarEvento"
    )
    try:
        nuevo_estado = transicionar(evento["estado"], evento_estado)
    except ErrorTransicion as error:
        raise ErrorRevision(str(error), "eventoNoRevisable") from error

    servicio = servicio_notificaciones or obtener_servicio_notificaciones(conexion)
    try:
        conexion.execute(
            "INSERT INTO revisiones_evento "
            "(evento_id, representante_id, decision, justificacion, fecha_revision) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                evento_id,
                usuario["id"],
                decision,
                justificacion_limpia or None,
                datetime.now(timezone.utc).isoformat(timespec="seconds"),
            ),
        )
        conexion.execute(
            "UPDATE eventos_ensayo SET estado = ? WHERE id = ?",
            (nuevo_estado, evento_id),
        )
        datos_evento = {
            "id": evento_id,
            "banda_id": evento["banda_id"],
            "fecha": evento["fecha"],
            "tipo": evento["tipo"],
            "estado": nuevo_estado,
        }
        if decision == DecisionRevision.APROBADA.value:
            # HU-08 CA3: se emiten las convocatorias y se notifica a los convocados.
            emitir_convocatorias(conexion, datos_evento, servicio)

        lideres = conexion.execute(
            "SELECT id, nombre FROM integrantes WHERE banda_id = ? AND rol = ? "
            "ORDER BY id",
            (evento["banda_id"], RolIntegrante.LIDER.value),
        ).fetchall()
        servicio.enviar_resultado_revision(
            lideres, datos_evento, decision, justificacion_limpia or None
        )
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise

    return ResultadoRevision(evento_id=evento_id, decision=decision, estado=nuevo_estado)
