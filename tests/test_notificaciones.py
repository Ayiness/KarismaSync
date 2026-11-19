from app.integraciones.notificaciones import ServicioNotificacionesSimulado


def test_envio_de_convocatoria_registra_solicitud_y_entregas(conexion):
    destinatarios = conexion.execute(
        "SELECT id, nombre FROM integrantes ORDER BY id"
    ).fetchall()
    servicio = ServicioNotificacionesSimulado(conexion)

    respuesta = servicio.enviar_convocatoria(
        destinatarios,
        {"id": 1, "fecha": "2026-11-14"},
        "/eventos/1",
    )
    conexion.commit()

    assert respuesta.aceptada is True
    assert respuesta.mensaje == "solicitudAceptada"

    filas = conexion.execute(
        "SELECT mensaje FROM integraciones_log ORDER BY id"
    ).fetchall()
    assert [fila["mensaje"] for fila in filas] == ["enviarConvocatoria"] + [
        "entrega convocatoria"
    ] * len(destinatarios)
    assert len(destinatarios) == 6
