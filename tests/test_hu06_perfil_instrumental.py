"""Pruebas de aceptación de HU-06 — Registrar el perfil instrumental del integrante.

Una prueba por escenario Gherkin de `07-criterios-aceptacion.md` (HU-06).
"""

from tests.helpers import id_de, id_instrumento


def _instrumento_principal(conexion, integrante_id):
    fila = conexion.execute(
        "SELECT instrumento_id FROM integrantes_instrumentos WHERE integrante_id = ?",
        (integrante_id,),
    ).fetchone()
    return fila["instrumento_id"] if fila else None


def _sin_perfil(conexion, integrante_id):
    """Deja al integrante sin perfil instrumental (el seed le asigna uno)."""
    conexion.execute(
        "DELETE FROM integrantes_instrumentos WHERE integrante_id = ?",
        (integrante_id,),
    )
    conexion.commit()


def test_hu06_el_integrante_registra_su_instrumento_principal(conexion, cliente):
    # Dado que Pedro es integrante de la banda y todavía no tiene un perfil instrumental
    pedro = id_de(conexion, "Pedro")
    _sin_perfil(conexion, pedro)
    guitarra_electrica = id_instrumento(conexion, "guitarra eléctrica")
    cliente.cookies.set("usuario_id", str(pedro))

    # Cuando Pedro selecciona guitarra eléctrica como su instrumento principal
    respuesta = cliente.post(
        "/perfil",
        data={"instrumento_id": str(guitarra_electrica)},
        follow_redirects=False,
    )

    # Entonces el perfil de Pedro queda registrado con guitarra eléctrica
    assert respuesta.status_code == 303
    assert _instrumento_principal(conexion, pedro) == guitarra_electrica

    # Y el Líder de Alabanza puede ver ese instrumento al crear un evento de ensayo
    cliente.cookies.set("usuario_id", str(id_de(conexion, "Marta")))
    formulario = cliente.get("/eventos/nuevo")
    assert formulario.status_code == 200
    assert "Pedro" in formulario.text
    assert "Instrumento principal: guitarra eléctrica" in formulario.text


def test_hu06_el_integrante_cambia_su_instrumento_principal(conexion, cliente):
    # Dado que Pedro tiene registrado guitarra eléctrica como su instrumento principal
    pedro = id_de(conexion, "Pedro")
    assert _instrumento_principal(conexion, pedro) == id_instrumento(
        conexion, "guitarra eléctrica"
    )
    guitarra_acustica = id_instrumento(conexion, "guitarra acústica")
    cliente.cookies.set("usuario_id", str(pedro))

    # Cuando Pedro cambia su instrumento principal a guitarra acústica
    respuesta = cliente.post(
        "/perfil",
        data={"instrumento_id": str(guitarra_acustica)},
        follow_redirects=False,
    )

    # Entonces el perfil de Pedro queda con guitarra acústica como instrumento principal
    assert respuesta.status_code == 303
    assert _instrumento_principal(conexion, pedro) == guitarra_acustica


def test_hu06_el_integrante_intenta_registrar_su_perfil_sin_instrumento_principal(
    conexion, cliente
):
    # Dado que Pedro es integrante de la banda y todavía no tiene un perfil instrumental
    pedro = id_de(conexion, "Pedro")
    _sin_perfil(conexion, pedro)
    cliente.cookies.set("usuario_id", str(pedro))

    # Cuando Pedro intenta guardar su perfil sin indicar un instrumento principal
    respuesta = cliente.post("/perfil", data={}, follow_redirects=False)

    # Entonces el perfil de Pedro no queda registrado
    assert respuesta.status_code == 200
    assert _instrumento_principal(conexion, pedro) is None
    # Y Pedro es informado de que debe indicar un instrumento principal
    assert "debe indicar un instrumento principal" in respuesta.text
