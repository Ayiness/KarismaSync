"""EST-02 — Ciclo de vida de la asistencia: transiciones válidas e inválidas."""

import pytest

from app.dominio.asistencia import ESTADO_INICIAL, transicionar
from app.dominio.evento_ensayo import ErrorTransicion


def test_convocatoria_emitida_deja_la_asistencia_pendiente():
    assert transicionar(ESTADO_INICIAL, "convocatoriaEmitida") == "Pendiente"


def test_transiciones_validas_de_registrar_asistencia():
    assert transicionar("Pendiente", "registrarAsistencia", True) == "Confirmada"
    assert transicionar("Pendiente", "registrarAsistencia", False) == "No asiste"
    assert transicionar("Confirmada", "registrarAsistencia", False) == "No asiste"
    assert transicionar("No asiste", "registrarAsistencia", True) == "Confirmada"


def test_repetir_la_misma_respuesta_es_una_transicion_no_modelada():
    with pytest.raises(ErrorTransicion, match="ya registraste esa respuesta"):
        transicionar("Confirmada", "registrarAsistencia", True)


def test_no_se_responde_desde_sin_respuesta():
    with pytest.raises(ErrorTransicion):
        transicionar("Sin respuesta", "registrarAsistencia", True)
