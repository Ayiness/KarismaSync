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
