from tests.helpers import id_de, id_instrumento


def test_inicio_lista_los_seis_integrantes(conexion, cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    for nombre in ["Marta", "Pedro", "Ana", "Luis", "Sofía", "Diego"]:
        assert nombre in respuesta.text
    assert respuesta.text.count("<option value=") == 7


def test_selector_de_usuario_conserva_la_eleccion(conexion, cliente):
    marta = id_de(conexion, "Marta")

    cambio = cliente.post(
        "/demo/usuario", data={"usuario_id": str(marta)}, follow_redirects=False
    )
    inicio = cliente.get("/")

    assert cambio.status_code == 303
    assert f'value="{marta}" selected' in inicio.text
    assert "Marta (Líder de Alabanza)" in inicio.text


def test_formulario_muestra_los_musicos_con_su_instrumento_principal(conexion, cliente):
    respuesta = cliente.get("/eventos/nuevo")

    assert respuesta.status_code == 200
    for nombre in ["Marta", "Pedro", "Ana", "Luis", "Sofía", "Diego"]:
        assert nombre in respuesta.text
    for instrumento in [
        "batería",
        "bajo",
        "guitarra eléctrica",
        "guitarra acústica",
        "teclado",
        "voz",
    ]:
        assert instrumento in respuesta.text
    assert "Instrumento principal" in respuesta.text


def test_perfil_requiere_usuario_de_demostracion(conexion, cliente):
    respuesta = cliente.get("/perfil")

    assert respuesta.status_code == 200
    assert "Elige un usuario de demostración" in respuesta.text


def test_perfil_registra_y_cambia_el_instrumento_principal(conexion, cliente):
    pedro = id_de(conexion, "Pedro")
    cliente.cookies.set("usuario_id", str(pedro))

    respuesta = cliente.post(
        "/perfil",
        data={"instrumento_id": str(id_instrumento(conexion, "guitarra acústica"))},
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    fila = conexion.execute(
        "SELECT instrumento_id FROM integrantes_instrumentos WHERE integrante_id = ?",
        (pedro,),
    ).fetchone()
    assert fila["instrumento_id"] == id_instrumento(conexion, "guitarra acústica")


def test_perfil_sin_instrumento_no_guarda(conexion, cliente):
    pedro = id_de(conexion, "Pedro")
    cliente.cookies.set("usuario_id", str(pedro))

    respuesta = cliente.post("/perfil", data={}, follow_redirects=False)

    assert respuesta.status_code == 200
    assert "debe indicar un instrumento principal" in respuesta.text
    fila = conexion.execute(
        "SELECT instrumento_id FROM integrantes_instrumentos WHERE integrante_id = ?",
        (pedro,),
    ).fetchone()
    assert fila["instrumento_id"] == id_instrumento(conexion, "guitarra eléctrica")
