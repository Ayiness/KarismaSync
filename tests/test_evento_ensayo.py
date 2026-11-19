import pytest

from app.dominio.evento_ensayo import (
    EstadoEvento,
    EventoDeEnsayo,
    ErrorTransicion,
    transicionar,
)


def test_crear_evento_lleva_de_inicial_a_vigente():
    evento = EventoDeEnsayo(banda_id=1, fecha="2026-11-14", quorum=4)

    assert evento.estado == "Inicial"
    assert transicionar(evento, "crearEvento") == EstadoEvento.VIGENTE.value
    assert evento.estado == EstadoEvento.VIGENTE.value


def test_transicion_no_permitida_falla_con_mensaje_claro():
    evento = EventoDeEnsayo(banda_id=1, fecha="2026-11-14", quorum=4)

    with pytest.raises(ErrorTransicion, match="Transición no permitida"):
        transicionar(evento, "cancelacionRegistrada")
