from dataclasses import dataclass
from enum import Enum

ESTADO_INICIAL = "Inicial"


class EstadoEvento(str, Enum):
    VIGENTE = "Vigente"
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"
    TERMINADO = "Terminado"


class ErrorTransicion(ValueError):
    pass


@dataclass
class EventoDeEnsayo:
    banda_id: int
    fecha: str
    quorum: int
    id: int | None = None
    estado: str = ESTADO_INICIAL


TRANSICIONES = {
    (ESTADO_INICIAL, "crearEvento"): EstadoEvento.VIGENTE.value,
}


def transicionar(evento: EventoDeEnsayo | str, evento_estado: str) -> str:
    estado_actual = evento.estado if isinstance(evento, EventoDeEnsayo) else str(evento)
    destino = TRANSICIONES.get((estado_actual, evento_estado))
    if destino is None:
        raise ErrorTransicion(
            f"Transición no permitida: {estado_actual} --{evento_estado}-->"
        )
    if isinstance(evento, EventoDeEnsayo):
        evento.estado = destino
    return destino
