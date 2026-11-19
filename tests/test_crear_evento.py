import pytest

from app.servicios.crear_evento import (
    Convocado,
    DatosNuevoEvento,
    ErrorCreacionEvento,
    crear_evento,
)
from tests.helpers import id_de, id_instrumento


def _conteo_eventos(conexion):
    return conexion.execute("SELECT COUNT(*) FROM eventos_ensayo").fetchone()[0]


def _convocado(conexion, nombre, instrumentos):
    return Convocado(
        integrante_id=id_de(conexion, nombre),
        instrumentos_ids=[id_instrumento(conexion, instrumento) for instrumento in instrumentos],
    )


def test_integrante_sin_rol_de_lider_no_crea(conexion):
    pedro = id_de(conexion, "Pedro")
    bateria = id_instrumento(conexion, "batería")

    with pytest.raises(ErrorCreacionEvento, match="solo el Líder de Alabanza"):
        crear_evento(
            conexion,
            pedro,
            DatosNuevoEvento(
                fecha="2026-11-14",
                quorum="4",
                convocados=[Convocado(integrante_id=pedro, instrumentos_ids=[bateria])],
            ),
        )

    assert _conteo_eventos(conexion) == 0


def test_sin_musicos_convocados_no_crea(conexion):
    marta = id_de(conexion, "Marta")

    with pytest.raises(ErrorCreacionEvento, match="debe convocar al menos un músico"):
        crear_evento(
            conexion,
            marta,
            DatosNuevoEvento(fecha="2026-11-14", quorum="4", convocados=[]),
        )

    assert _conteo_eventos(conexion) == 0


def test_musico_convocado_sin_instrumentos_no_crea(conexion):
    marta = id_de(conexion, "Marta")

    with pytest.raises(
        ErrorCreacionEvento, match="cada músico convocado debe tener al menos un instrumento"
    ):
        crear_evento(
            conexion,
            marta,
            DatosNuevoEvento(
                fecha="2026-11-14",
                quorum="4",
                convocados=[Convocado(integrante_id=id_de(conexion, "Pedro"))],
            ),
        )

    assert _conteo_eventos(conexion) == 0


def test_quorum_invalido_no_crea(conexion):
    marta = id_de(conexion, "Marta")

    with pytest.raises(ErrorCreacionEvento, match="debe indicar el quórum requerido"):
        crear_evento(
            conexion,
            marta,
            DatosNuevoEvento(
                fecha="2026-11-14",
                quorum="0",
                convocados=[_convocado(conexion, "Pedro", ["guitarra eléctrica"])],
            ),
        )

    assert _conteo_eventos(conexion) == 0


def test_quorum_vacio_usa_la_cantidad_de_convocados(conexion):
    marta = id_de(conexion, "Marta")

    resultado = crear_evento(
        conexion,
        marta,
        DatosNuevoEvento(
            fecha="2026-11-14",
            quorum="",
            convocados=[
                _convocado(conexion, "Pedro", ["guitarra eléctrica"]),
                _convocado(conexion, "Ana", ["teclado"]),
            ],
        ),
    )

    evento = conexion.execute(
        "SELECT * FROM eventos_ensayo WHERE id = ?", (resultado.evento_id,)
    ).fetchone()
    assert evento["quorum"] == 2


def test_fecha_invalida_no_crea(conexion):
    marta = id_de(conexion, "Marta")

    with pytest.raises(ErrorCreacionEvento, match="debe indicar una fecha válida"):
        crear_evento(
            conexion,
            marta,
            DatosNuevoEvento(
                fecha="no-es-fecha",
                quorum="4",
                convocados=[_convocado(conexion, "Pedro", ["guitarra eléctrica"])],
            ),
        )

    assert _conteo_eventos(conexion) == 0
