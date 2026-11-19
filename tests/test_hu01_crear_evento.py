from tests.helpers import id_de, id_instrumento

PERFIL = {
    "Marta": "voz",
    "Pedro": "guitarra eléctrica",
    "Ana": "teclado",
    "Luis": "batería",
    "Sofía": "bajo",
    "Diego": "guitarra acústica",
}
TODOS = list(PERFIL)


def _datos_formulario(conexion, fecha="2026-11-14", quorum="4", convocados=None, instrumentos_extra=None):
    instrumentos_extra = instrumentos_extra or {}
    if convocados is None:
        convocados = TODOS
    datos = {"fecha": fecha, "quorum": quorum, "convocados": []}
    for nombre in convocados:
        integrante_id = id_de(conexion, nombre)
        datos["convocados"].append(str(integrante_id))
        instrumentos = instrumentos_extra.get(nombre, [PERFIL[nombre]])
        if instrumentos:
            datos[f"instrumentos_{integrante_id}"] = [
                str(id_instrumento(conexion, instrumento))
                for instrumento in instrumentos
            ]
    return datos


def _conteo(conexion, tabla):
    return conexion.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]


def test_hu01_el_lider_crea_evento_y_convoca_a_toda_la_banda(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, quorum="6"),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert evento is not None
    assert evento["estado"] == "Vigente"
    assert evento["fecha"] == "2026-11-14"
    assert evento["quorum"] == 6
    assert respuesta.headers["location"] == f"/eventos/{evento['id']}"

    roles = {
        fila["nombre"]
        for fila in conexion.execute(
            "SELECT i.nombre FROM eventos_requieren_instrumentos r "
            "JOIN instrumentos i ON i.id = r.instrumento_id WHERE r.evento_id = ?",
            (evento["id"],),
        )
    }
    assert roles == set(PERFIL.values())
    assert _conteo(conexion, "convocatorias") == 6

    solicitudes = conexion.execute(
        "SELECT COUNT(*) FROM integraciones_log WHERE mensaje = 'enviarConvocatoria'"
    ).fetchone()[0]
    entregas = conexion.execute(
        "SELECT COUNT(*) FROM integraciones_log WHERE mensaje = 'entrega convocatoria'"
    ).fetchone()[0]
    assert solicitudes == 1
    assert entregas == 6

    detalle = cliente.get(f"/eventos/{evento['id']}")
    assert detalle.status_code == 200
    assert "Vigente" in detalle.text
    assert "guitarra eléctrica" in detalle.text
    assert "Pedro" in detalle.text


def test_hu01_el_lider_convoca_solo_a_los_musicos_que_necesita(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    seleccionados = ["Marta", "Pedro", "Ana", "Luis"]
    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, quorum="4", convocados=seleccionados),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    convocados = {
        fila["nombre"]
        for fila in conexion.execute(
            "SELECT i.nombre FROM convocatorias c "
            "JOIN integrantes i ON i.id = c.integrante_id WHERE c.evento_id = ?",
            (evento["id"],),
        )
    }
    assert convocados == set(seleccionados)
    assert _conteo(conexion, "convocatorias") == 4
    assert "Sofía" not in convocados
    assert "Diego" not in convocados


def test_hu01_el_lider_cambia_o_suma_instrumentos_a_un_convocado(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(
            conexion,
            quorum="1",
            convocados=["Pedro"],
            instrumentos_extra={"Pedro": ["guitarra acústica", "voz"]},
        ),
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    instrumentos = {
        fila["nombre"]
        for fila in conexion.execute(
            "SELECT i.nombre FROM convocatorias c "
            "JOIN convocatorias_instrumentos ci ON ci.convocatoria_id = c.id "
            "JOIN instrumentos i ON i.id = ci.instrumento_id "
            "WHERE c.evento_id = ? AND c.integrante_id = ?",
            (evento["id"], id_de(conexion, "Pedro")),
        )
    }
    assert instrumentos == {"guitarra acústica", "voz"}


def test_hu01_integrante_sin_rol_de_lider_no_crea_evento(conexion, cliente):
    pedro = id_de(conexion, "Pedro")
    cliente.cookies.set("usuario_id", str(pedro))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(conexion),
        follow_redirects=False,
    )

    assert respuesta.status_code == 200
    assert "solo el Líder de Alabanza puede crear eventos de ensayo" in respuesta.text
    assert _conteo(conexion, "eventos_ensayo") == 0
    assert _conteo(conexion, "convocatorias") == 0
    assert _conteo(conexion, "integraciones_log") == 0


def test_hu01_lider_sin_musicos_convocados_no_crea_evento(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data={"fecha": "2026-11-14", "quorum": "4"},
        follow_redirects=False,
    )

    assert respuesta.status_code == 200
    assert "debe convocar al menos un músico" in respuesta.text
    assert _conteo(conexion, "eventos_ensayo") == 0
    assert _conteo(conexion, "convocatorias") == 0


def test_hu01_lider_con_musico_convocado_sin_instrumentos_no_crea_evento(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    respuesta = cliente.post(
        "/eventos",
        data=_datos_formulario(
            conexion,
            quorum="1",
            convocados=["Ana"],
            instrumentos_extra={"Ana": []},
        ),
        follow_redirects=False,
    )

    assert respuesta.status_code == 200
    assert "cada músico convocado debe tener al menos un instrumento" in respuesta.text
    assert _conteo(conexion, "eventos_ensayo") == 0


def test_hu01_quorum_vacio_usa_la_cantidad_de_convocados(conexion, cliente):
    marta = id_de(conexion, "Marta")
    cliente.cookies.set("usuario_id", str(marta))

    cliente.post(
        "/eventos",
        data=_datos_formulario(conexion, quorum="", convocados=["Pedro", "Ana"]),
        follow_redirects=False,
    )

    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert evento["quorum"] == 2
