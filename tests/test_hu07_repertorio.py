from tests.helpers import id_cancion, id_de, id_instrumento

PERFIL = {
    "Marta": "voz",
    "Pedro": "guitarra eléctrica",
    "Ana": "teclado",
    "Luis": "batería",
    "Sofía": "bajo",
    "Diego": "guitarra acústica",
}
CONVOCADOS = ["Marta", "Pedro", "Ana", "Luis"]


def _datos_formulario(
    conexion,
    fecha="2026-11-14",
    quorum="4",
    convocados=None,
    canciones=None,
    incluir_repertorio=True,
):
    if convocados is None:
        convocados = CONVOCADOS
    datos = {"fecha": fecha, "quorum": quorum, "convocados": []}
    for nombre in convocados:
        integrante_id = id_de(conexion, nombre)
        datos["convocados"].append(str(integrante_id))
        datos[f"instrumentos_{integrante_id}"] = [
            str(id_instrumento(conexion, PERFIL[nombre]))
        ]
    if incluir_repertorio:
        datos["incluir_repertorio"] = "1"
    if canciones:
        datos["canciones"] = [
            str(id_cancion(conexion, titulo)) for titulo in canciones
        ]
    return datos


def _titulos_del_evento(conexion, evento_id):
    return {
        fila["titulo"]
        for fila in conexion.execute(
            "SELECT c.titulo FROM eventos_canciones ec "
            "JOIN canciones c ON c.id = ec.cancion_id "
            "WHERE ec.evento_id = ?",
            (evento_id,),
        )
    }


def test_hu07_formulario_ofrece_repertorio_activo_y_catalogo_de_20(conexion, cliente):
    respuesta = cliente.get("/eventos/nuevo")

    assert respuesta.status_code == 200
    assert respuesta.text.count('name="canciones"') == 20
    assert 'id="incluir-repertorio"' in respuesta.text
    assert 'name="incluir_repertorio"' in respuesta.text
    assert "checked" in respuesta.text
    assert "Cuán grande es Él" in respuesta.text


def test_hu07_lider_crea_evento_con_canciones_seleccionadas(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))
    titulos = ["Cuán grande es Él", "Sublime gracia"]

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, canciones=titulos),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert _titulos_del_evento(conexion, evento["id"]) == set(titulos)

    detalle = cliente.get(f"/eventos/{evento['id']}")
    assert detalle.status_code == 200
    for titulo in titulos:
        assert titulo in detalle.text


def test_hu07_canciones_no_seleccionadas_no_se_asocian(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, canciones=["Cuán grande es Él"]),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert _titulos_del_evento(conexion, evento["id"]) == {"Cuán grande es Él"}
    assert "Sublime gracia" not in _titulos_del_evento(conexion, evento["id"])


def test_hu07_lider_crea_evento_sin_repertorio_al_desactivar(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, incluir_repertorio=False),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert _titulos_del_evento(conexion, evento["id"]) == set()

    detalle = cliente.get(f"/eventos/{evento['id']}")
    assert "Este evento no incluye repertorio de canciones." in detalle.text


def test_hu07_lider_deja_repertorio_activo_sin_canciones(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, incluir_repertorio=True),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert _titulos_del_evento(conexion, evento["id"]) == set()

    detalle = cliente.get(f"/eventos/{evento['id']}")
    assert "Este evento no incluye repertorio de canciones." in detalle.text
