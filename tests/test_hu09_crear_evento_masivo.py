"""HU-09 — Crear un evento masivo (07-criterios-aceptacion.md)."""

import json

from app.dominio.evento_ensayo import EstadoEvento, EventoDeEnsayo, transicionar
from tests.helpers import id_de, id_instrumento

PERFIL = {
    "Marta": "voz",
    "Pedro": "guitarra eléctrica",
    "Ana": "teclado",
    "Luis": "batería",
    "Sofía": "bajo",
    "Diego": "guitarra acústica",
}


def datos_evento(conexion, tipo="Masivo", fecha="2026-12-12", quorum="6"):
    datos = {"tipo": tipo, "fecha": fecha, "quorum": quorum, "convocados": []}
    for nombre, instrumento in PERFIL.items():
        integrante_id = id_de(conexion, nombre)
        datos["convocados"].append(str(integrante_id))
        datos[f"instrumentos_{integrante_id}"] = [str(id_instrumento(conexion, instrumento))]
    return datos


def como(cliente, conexion, nombre):
    cliente.cookies.set("usuario_id", str(id_de(conexion, nombre)))


def mensajes_log(conexion):
    return [
        (fila["mensaje"], json.loads(fila["detalle"]))
        for fila in conexion.execute(
            "SELECT mensaje, detalle FROM integraciones_log ORDER BY id"
        )
    ]


def test_dominio_crear_evento_decide_por_tipo():
    ensayo = EventoDeEnsayo(banda_id=1, fecha="2026-12-05", quorum=4, tipo="Ensayo")
    masivo = EventoDeEnsayo(banda_id=1, fecha="2026-12-12", quorum=4, tipo="Masivo")

    assert transicionar(ensayo, "crearEvento") == EstadoEvento.VIGENTE.value
    assert transicionar(masivo, "crearEvento") == EstadoEvento.PENDIENTE_APROBACION.value
    assert transicionar(masivo.estado, "aprobarEvento") == EstadoEvento.VIGENTE.value
    assert transicionar(masivo.estado, "rechazarEvento") == EstadoEvento.RECHAZADO.value


def test_hu09_el_formulario_propone_el_tipo_ensayo_por_defecto(conexion, cliente):
    como(cliente, conexion, "Marta")

    respuesta = cliente.get("/eventos/nuevo")

    assert respuesta.status_code == 200
    assert 'name="tipo" value="Ensayo" checked' in respuesta.text
    assert 'name="tipo" value="Masivo"' in respuesta.text
    assert 'name="tipo" value="Masivo" checked' not in respuesta.text


def test_hu09_el_lider_crea_un_evento_masivo_que_queda_pendiente(conexion, cliente):
    como(cliente, conexion, "Marta")

    respuesta = cliente.post(
        "/eventos", data=datos_evento(conexion), follow_redirects=False
    )

    assert respuesta.status_code == 303
    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert evento["tipo"] == "Masivo"
    assert evento["estado"] == "Pendiente de aprobación"
    # Los convocados quedan registrados con sus instrumentos, pero sin asistencia:
    # todavía no reciben la convocatoria.
    assert conexion.execute("SELECT COUNT(*) FROM convocatorias").fetchone()[0] == 6
    assert conexion.execute("SELECT COUNT(*) FROM asistencias").fetchone()[0] == 0
    log = mensajes_log(conexion)
    assert [mensaje for mensaje, _ in log] == ["enviarSolicitudRevision"]
    assert log[0][1]["representante"] == "Andrés"


def test_hu09_los_convocados_no_ven_ni_responden_el_evento_pendiente(conexion, cliente):
    como(cliente, conexion, "Marta")
    cliente.post("/eventos", data=datos_evento(conexion))
    evento_id = conexion.execute("SELECT id FROM eventos_ensayo").fetchone()["id"]

    como(cliente, conexion, "Pedro")
    assert f"/eventos/{evento_id}" not in cliente.get("/").text
    assert cliente.get(f"/eventos/{evento_id}").status_code == 404
    respuesta = cliente.post(
        f"/eventos/{evento_id}/asistencia", data={"respuesta": "confirmar"}
    )
    assert respuesta.status_code == 404

    import pytest

    from app.servicios.registrar_asistencia import ErrorRespuesta, registrar_asistencia

    with pytest.raises(ErrorRespuesta) as error:
        registrar_asistencia(conexion, id_de(conexion, "Pedro"), evento_id, asiste=True)
    assert error.value.motivo == "convocatoriaNoDisponible"
    assert conexion.execute("SELECT COUNT(*) FROM asistencias").fetchone()[0] == 0


def test_hu09_el_lider_crea_un_ensayo_y_no_pasa_por_revision(conexion, cliente):
    como(cliente, conexion, "Marta")

    cliente.post("/eventos", data=datos_evento(conexion, tipo="Ensayo", fecha="2026-12-05"))

    evento = conexion.execute("SELECT * FROM eventos_ensayo").fetchone()
    assert evento["tipo"] == "Ensayo"
    assert evento["estado"] == "Vigente"
    assert conexion.execute("SELECT COUNT(*) FROM asistencias").fetchone()[0] == 6
    mensajes = [mensaje for mensaje, _ in mensajes_log(conexion)]
    assert "enviarSolicitudRevision" not in mensajes
    assert mensajes[0] == "enviarConvocatoria"


def test_hu09_banda_sin_representante_no_puede_crear_evento_masivo(conexion, cliente):
    conexion.execute(
        "UPDATE integrantes SET rol = 'Músico' WHERE rol = 'Representante de músicos'"
    )
    conexion.commit()
    como(cliente, conexion, "Marta")

    respuesta = cliente.post("/eventos", data=datos_evento(conexion))

    assert respuesta.status_code == 200
    assert "la banda necesita un Representante de músicos" in respuesta.text
    assert conexion.execute("SELECT COUNT(*) FROM eventos_ensayo").fetchone()[0] == 0


def test_hu09_el_evento_masivo_valida_los_mismos_datos(conexion, cliente):
    como(cliente, conexion, "Marta")

    respuesta = cliente.post("/eventos", data=datos_evento(conexion, quorum=""))

    assert "debe indicar el quórum requerido" in respuesta.text
    assert conexion.execute("SELECT COUNT(*) FROM eventos_ensayo").fetchone()[0] == 0


def test_hu09_el_lider_ve_el_estado_de_su_evento_masivo(conexion, cliente):
    como(cliente, conexion, "Marta")
    cliente.post("/eventos", data=datos_evento(conexion))
    evento_id = conexion.execute("SELECT id FROM eventos_ensayo").fetchone()["id"]

    respuesta = cliente.get(f"/eventos/{evento_id}")

    assert respuesta.status_code == 200
    assert "Evento masivo" in respuesta.text
    assert "Pendiente de aprobación" in respuesta.text
    assert "Aprobar convocatoria" not in respuesta.text


def test_un_representante_por_banda(conexion):
    import sqlite3

    import pytest

    with pytest.raises(sqlite3.IntegrityError):
        conexion.execute(
            "UPDATE integrantes SET rol = 'Representante de músicos' WHERE nombre = 'Pedro'"
        )
