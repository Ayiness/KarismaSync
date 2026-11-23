"""Ciclo de vida de la Asistencia (EST-02, HU-03)."""

from enum import Enum

from app.dominio.evento_ensayo import ErrorTransicion

ESTADO_INICIAL = "Inicial"


class EstadoAsistencia(str, Enum):
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    NO_ASISTE = "No asiste"
    SIN_RESPUESTA = "Sin respuesta"


# (estado origen, evento, asiste) -> estado destino.
# `asiste` distingue las guardas de registrarAsistencia: True = confirma,
# False = no asistirá e indica motivo. Es None en los eventos sin guarda.
TRANSICIONES = {
    (ESTADO_INICIAL, "convocatoriaEmitida", None): EstadoAsistencia.PENDIENTE.value,
    (EstadoAsistencia.PENDIENTE.value, "registrarAsistencia", True): EstadoAsistencia.CONFIRMADA.value,
    (EstadoAsistencia.PENDIENTE.value, "registrarAsistencia", False): EstadoAsistencia.NO_ASISTE.value,
    (EstadoAsistencia.CONFIRMADA.value, "registrarAsistencia", False): EstadoAsistencia.NO_ASISTE.value,
    (EstadoAsistencia.NO_ASISTE.value, "registrarAsistencia", True): EstadoAsistencia.CONFIRMADA.value,
    (EstadoAsistencia.PENDIENTE.value, "eventoCerrado", None): EstadoAsistencia.SIN_RESPUESTA.value,
}


def transicionar(estado_actual: str, evento: str, asiste: bool | None = None) -> str:
    destino = TRANSICIONES.get((estado_actual, evento, asiste))
    if destino is None:
        if evento == "registrarAsistencia":
            raise ErrorTransicion("ya registraste esa respuesta")
        raise ErrorTransicion(
            f"Transición no permitida: {estado_actual} --{evento}-->"
        )
    return destino
