"""Ciclo de vida del EventoDeEnsayo (EST-01, HU-01, HU-08, HU-09)."""

from dataclasses import dataclass
from enum import Enum

ESTADO_INICIAL = "Inicial"


class EstadoEvento(str, Enum):
    PENDIENTE_APROBACION = "Pendiente de aprobación"
    VIGENTE = "Vigente"
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"
    TERMINADO = "Terminado"
    RECHAZADO = "Rechazado"


class TipoEvento(str, Enum):
    ENSAYO = "Ensayo"
    MASIVO = "Masivo"


class ErrorTransicion(ValueError):
    pass


# Un evento está publicado cuando los convocados ya lo ven y pueden responder.
# Un evento masivo Pendiente de aprobación o Rechazado no está publicado (HU-09 CA3).
ESTADOS_NO_PUBLICADOS = {
    EstadoEvento.PENDIENTE_APROBACION.value,
    EstadoEvento.RECHAZADO.value,
}


@dataclass
class EventoDeEnsayo:
    banda_id: int
    fecha: str
    quorum: int
    tipo: str = TipoEvento.ENSAYO.value
    id: int | None = None
    estado: str = ESTADO_INICIAL


# (estado origen, evento, tipo) -> estado destino. `tipo` es la guarda del
# pseudoestado de decisión de EST-01; es None en las transiciones sin guarda de tipo.
TRANSICIONES = {
    (ESTADO_INICIAL, "crearEvento", TipoEvento.ENSAYO.value): EstadoEvento.VIGENTE.value,
    (ESTADO_INICIAL, "crearEvento", TipoEvento.MASIVO.value): EstadoEvento.PENDIENTE_APROBACION.value,
    (EstadoEvento.PENDIENTE_APROBACION.value, "aprobarEvento", None): EstadoEvento.VIGENTE.value,
    (EstadoEvento.PENDIENTE_APROBACION.value, "rechazarEvento", None): EstadoEvento.RECHAZADO.value,
}


def transicionar(
    evento: EventoDeEnsayo | str, evento_estado: str, tipo: str | None = None
) -> str:
    if isinstance(evento, EventoDeEnsayo):
        estado_actual = evento.estado
        if evento_estado == "crearEvento" and tipo is None:
            tipo = evento.tipo
    else:
        estado_actual = str(evento)
    if evento_estado == "crearEvento" and tipo is None:
        tipo = TipoEvento.ENSAYO.value
    clave_tipo = tipo if evento_estado == "crearEvento" else None
    destino = TRANSICIONES.get((estado_actual, evento_estado, clave_tipo))
    if destino is None:
        raise ErrorTransicion(
            f"Transición no permitida: {estado_actual} --{evento_estado}-->"
        )
    if isinstance(evento, EventoDeEnsayo):
        evento.estado = destino
    return destino
