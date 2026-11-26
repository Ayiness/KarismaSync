"""HU-08 — Confirmar la convocatoria de un evento masivo (07-criterios-aceptacion.md)."""

import json

from tests.helpers import id_de
from tests.test_hu09_crear_evento_masivo import como, datos_evento


def crear(conexion, cliente, tipo="Masivo", fecha="2026-12-12"):
    como(cliente, conexion, "Marta")
    cliente.post("/eventos", data=datos_evento(conexion, tipo=tipo, fecha=fecha))
    return conexion.execute(
        "SELECT id FROM eventos_ensayo WHERE fecha = ?", (fecha,)
    ).fetchone()["id"]


def estado(conexion, evento_id):
    return conexion.execute(
        "SELECT estado FROM eventos_ensayo WHERE id = ?", (evento_id,)
    ).fetchone()["estado"]


def ultimo_log(conexion, mensaje):
    fila = conexion.execute(
        "SELECT detalle FROM integraciones_log WHERE mensaje = ? ORDER BY id DESC",
        (mensaje,),
    ).fetchone()
    return json.loads(fila["detalle"]) if fila else None


def test_hu08_el_representante_solo_ve_los_masivos_pendientes(conexion, cliente):
    masivo = crear(conexion, cliente, "Masivo", "2026-12-12")
    ensayo = crear(conexion, cliente, "Ensayo", "2026-12-05")
    como(cliente, conexion, "Andrés")

    respuesta = cliente.get("/revisiones")

    assert respuesta.status_code == 200
    assert f"/eventos/{masivo}" in respuesta.text
    assert f"/eventos/{ensayo}" not in respuesta.text


def test_hu08_el_representante_ve_el_detalle_antes_de_decidir(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Andrés")

    respuesta = cliente.get(f"/eventos/{evento_id}")

    assert respuesta.status_code == 200
    assert "Aprobar convocatoria" in respuesta.text
    assert "Rechazar convocatoria" in respuesta.text
    for nombre in ["Pedro", "Ana", "Luis", "Sofía", "Diego"]:
        assert nombre in respuesta.text
    assert "batería" in respuesta.text


def test_hu08_el_representante_aprueba_un_evento_masivo(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Andrés")

    respuesta = cliente.post(
        f"/eventos/{evento_id}/revision",
        data={"decision": "Aprobada"},
        follow_redirects=False,
    )

    assert respuesta.status_code == 303
    assert estado(conexion, evento_id) == "Vigente"
    asistencias = conexion.execute("SELECT estado FROM asistencias").fetchall()
    assert len(asistencias) == 6
    assert {fila["estado"] for fila in asistencias} == {"Pendiente"}
    assert ultimo_log(conexion, "enviarConvocatoria")["evento"]["id"] == evento_id
    resultado = ultimo_log(conexion, "enviarResultadoRevision")
    assert resultado["decision"] == "Aprobada"
    assert resultado["lideres"] == [id_de(conexion, "Marta")]
    revision = conexion.execute("SELECT * FROM revisiones_evento").fetchone()
    assert revision["representante_id"] == id_de(conexion, "Andrés")

    # Ahora los convocados sí pueden responder.
    como(cliente, conexion, "Pedro")
    cliente.post(f"/eventos/{evento_id}/asistencia", data={"respuesta": "confirmar"})
    assert conexion.execute(
        "SELECT COUNT(*) FROM asistencias WHERE estado = 'Confirmada'"
    ).fetchone()[0] == 1


def test_hu08_el_representante_rechaza_con_justificacion(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Andrés")

    cliente.post(
        f"/eventos/{evento_id}/revision",
        data={"decision": "Rechazada", "justificacion": "Coincide con el concierto regional"},
    )

    assert estado(conexion, evento_id) == "Rechazado"
    assert conexion.execute("SELECT COUNT(*) FROM asistencias").fetchone()[0] == 0
    assert ultimo_log(conexion, "enviarConvocatoria") is None
    resultado = ultimo_log(conexion, "enviarResultadoRevision")
    assert resultado["decision"] == "Rechazada"
    assert resultado["justificacion"] == "Coincide con el concierto regional"

    como(cliente, conexion, "Marta")
    assert "Coincide con el concierto regional" in cliente.get(f"/eventos/{evento_id}").text


def test_hu08_rechazo_sin_justificacion_no_se_registra(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Andrés")

    respuesta = cliente.post(
        f"/eventos/{evento_id}/revision",
        data={"decision": "Rechazada", "justificacion": "   "},
    )

    assert "debe indicar la justificación del rechazo" in respuesta.text
    assert estado(conexion, evento_id) == "Pendiente de aprobación"
    assert conexion.execute("SELECT COUNT(*) FROM revisiones_evento").fetchone()[0] == 0


def test_hu08_un_evento_ya_aprobado_no_se_vuelve_a_revisar(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Andrés")
    cliente.post(f"/eventos/{evento_id}/revision", data={"decision": "Aprobada"})

    respuesta = cliente.post(
        f"/eventos/{evento_id}/revision",
        data={"decision": "Rechazada", "justificacion": "Cambio de planes"},
    )

    assert "el evento ya fue revisado" in respuesta.text
    assert estado(conexion, evento_id) == "Vigente"


def test_hu08_un_ensayo_no_se_revisa(conexion, cliente):
    evento_id = crear(conexion, cliente, "Ensayo", "2026-12-05")
    como(cliente, conexion, "Andrés")

    respuesta = cliente.post(f"/eventos/{evento_id}/revision", data={"decision": "Aprobada"})

    assert "no es masivo" in respuesta.text
    assert conexion.execute("SELECT COUNT(*) FROM revisiones_evento").fetchone()[0] == 0


def test_hu08_el_representante_no_puede_crear_eventos(conexion, cliente):
    como(cliente, conexion, "Andrés")

    respuesta = cliente.post("/eventos", data=datos_evento(conexion))

    assert "solo el Líder de Alabanza puede crear eventos" in respuesta.text
    assert conexion.execute("SELECT COUNT(*) FROM eventos_ensayo").fetchone()[0] == 0


def test_hu08_el_lider_no_puede_aprobar_su_propio_evento(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Marta")

    respuesta = cliente.post(f"/eventos/{evento_id}/revision", data={"decision": "Aprobada"})

    assert "solo el Representante de músicos de la banda" in respuesta.text
    assert estado(conexion, evento_id) == "Pendiente de aprobación"


def test_hu08_un_musico_no_puede_revisar(conexion, cliente):
    evento_id = crear(conexion, cliente)
    como(cliente, conexion, "Pedro")

    respuesta = cliente.post(f"/eventos/{evento_id}/revision", data={"decision": "Aprobada"})

    # Pedro no ve el evento sin publicar; el rechazo se muestra como no encontrado.
    assert respuesta.status_code == 404
    assert estado(conexion, evento_id) == "Pendiente de aprobación"
