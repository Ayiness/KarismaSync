"""Pruebas de aceptación de HU-03 — Confirmar asistencia al ensayo.

Una prueba por escenario Gherkin de `07-criterios-aceptacion.md` (HU-03).
"""

from app.servicios.crear_evento import Convocado, DatosNuevoEvento, crear_evento
from tests.helpers import id_de, id_instrumento


def _crear_evento(conexion, convocados):
    """Marta crea el evento del sábado 14 de noviembre con los convocados indicados.

    `convocados` es un dict {nombre: [instrumentos]}.
    """
    resultado = crear_evento(
        conexion,
        id_de(conexion, "Marta"),
        DatosNuevoEvento(
            fecha="2026-11-14",
            quorum=str(len(convocados)),
            convocados=[
                Convocado(
                    integrante_id=id_de(conexion, nombre),
                    instrumentos_ids=[id_instrumento(conexion, i) for i in instrumentos],
                )
                for nombre, instrumentos in convocados.items()
            ],
        ),
    )
    return resultado.evento_id


def _como(cliente, conexion, nombre):
    cliente.cookies.set("usuario_id", str(id_de(conexion, nombre)))


def _responder(cliente, evento_id, respuesta, motivo=None, instrumentos=None):
    datos = {"respuesta": respuesta}
    if motivo is not None:
        datos["motivo"] = motivo
    if instrumentos is not None:
        datos["instrumentos"] = [str(i) for i in instrumentos]
    return cliente.post(
        f"/eventos/{evento_id}/asistencia", data=datos, follow_redirects=False
    )


def _asistencia(conexion, evento_id, nombre):
    return conexion.execute(
        "SELECT a.estado, a.motivo FROM asistencias a "
        "JOIN convocatorias c ON c.id = a.convocatoria_id "
        "WHERE c.evento_id = ? AND c.integrante_id = ?",
        (evento_id, id_de(conexion, nombre)),
    ).fetchone()


def _instrumentos_convocatoria(conexion, evento_id, nombre):
    filas = conexion.execute(
        "SELECT i.nombre FROM convocatorias c "
        "JOIN convocatorias_instrumentos ci ON ci.convocatoria_id = c.id "
        "JOIN instrumentos i ON i.id = ci.instrumento_id "
        "WHERE c.evento_id = ? AND c.integrante_id = ? ORDER BY i.nombre",
        (evento_id, id_de(conexion, nombre)),
    ).fetchall()
    return [fila["nombre"] for fila in filas]


def test_hu03_el_integrante_confirma_su_asistencia_y_ve_los_instrumentos_asignados(
    conexion, cliente
):
    # Dado que el evento está vigente y Pedro fue convocado con guitarra eléctrica y voz
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica", "voz"]})
    _como(cliente, conexion, "Pedro")

    # Cuando Pedro confirma que asistirá al ensayo
    respuesta = _responder(cliente, evento_id, "confirmar")

    # Entonces Pedro queda registrado como asistente del ensayo
    assert respuesta.status_code == 303
    assert _asistencia(conexion, evento_id, "Pedro")["estado"] == "Confirmada"
    # Y guitarra eléctrica y voz quedan registrados como sus instrumentos para ese ensayo
    assert _instrumentos_convocatoria(conexion, evento_id, "Pedro") == [
        "guitarra eléctrica",
        "voz",
    ]
    detalle = cliente.get(f"/eventos/{evento_id}")
    assert "Tus instrumentos" in detalle.text
    assert "guitarra eléctrica, voz" in detalle.text
    # Y su respuesta queda considerada (guardada y consultable) para la evaluación del quórum (HU-04)
    confirmadas = conexion.execute(
        "SELECT COUNT(*) FROM asistencias a JOIN convocatorias c ON c.id = a.convocatoria_id "
        "WHERE c.evento_id = ? AND a.estado = 'Confirmada'",
        (evento_id,),
    ).fetchone()[0]
    assert confirmadas == 1


def test_hu03_el_integrante_informa_que_no_asistira(conexion, cliente):
    # Dado que el evento está vigente y Pedro fue convocado con guitarra eléctrica
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica"]})
    _como(cliente, conexion, "Pedro")

    # Cuando Pedro informa que no asistirá porque «tengo turno en el trabajo»
    respuesta = _responder(
        cliente, evento_id, "no_asistire", motivo="tengo turno en el trabajo"
    )

    # Entonces queda registrado como no asistente con el motivo
    assert respuesta.status_code == 303
    asistencia = _asistencia(conexion, evento_id, "Pedro")
    assert asistencia["estado"] == "No asiste"
    assert asistencia["motivo"] == "tengo turno en el trabajo"
    # Y no se registran instrumentos a su nombre para ese ensayo
    confirmadas = conexion.execute(
        "SELECT COUNT(*) FROM asistencias WHERE estado = 'Confirmada'"
    ).fetchone()[0]
    assert confirmadas == 0


def test_hu03_el_integrante_intenta_informar_que_no_asistira_sin_indicar_el_motivo(
    conexion, cliente
):
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica"]})
    _como(cliente, conexion, "Pedro")

    # Cuando Pedro informa que no asistirá sin escribir un motivo
    respuesta = _responder(cliente, evento_id, "no_asistire", motivo="   ")

    # Entonces la respuesta no queda registrada y su asistencia sigue pendiente
    assert respuesta.status_code == 200
    asistencia = _asistencia(conexion, evento_id, "Pedro")
    assert asistencia["estado"] == "Pendiente"
    assert asistencia["motivo"] is None
    # Y Pedro es informado de que debe indicar el motivo
    assert "debe indicar el motivo por el que no asistirá" in respuesta.text


def test_hu03_el_integrante_cambia_su_respuesta_de_confirmada_a_no_asiste(
    conexion, cliente
):
    # Dado que el evento está vigente y Pedro confirmó su asistencia
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica"]})
    _como(cliente, conexion, "Pedro")
    _responder(cliente, evento_id, "confirmar")
    assert "Cambiar respuesta: no asistiré" in cliente.get(f"/eventos/{evento_id}").text

    # Cuando Pedro cambia su respuesta e informa que no asistirá porque «me enfermé»
    respuesta = _responder(cliente, evento_id, "no_asistire", motivo="me enfermé")

    # Entonces queda registrado como no asistente con el motivo «me enfermé»
    assert respuesta.status_code == 303
    asistencia = _asistencia(conexion, evento_id, "Pedro")
    assert asistencia["estado"] == "No asiste"
    assert asistencia["motivo"] == "me enfermé"


def test_hu03_el_integrante_cambia_su_respuesta_de_no_asiste_a_confirmada(
    conexion, cliente
):
    # Dado que el evento está vigente y Pedro informó que no asistirá con un motivo
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica"]})
    _como(cliente, conexion, "Pedro")
    _responder(cliente, evento_id, "no_asistire", motivo="tengo turno en el trabajo")
    assert (
        "Cambiar respuesta: confirmar asistencia"
        in cliente.get(f"/eventos/{evento_id}").text
    )

    # Cuando Pedro cambia su respuesta y confirma que asistirá
    respuesta = _responder(cliente, evento_id, "confirmar")

    # Entonces Pedro queda registrado como asistente
    assert respuesta.status_code == 303
    asistencia = _asistencia(conexion, evento_id, "Pedro")
    assert asistencia["estado"] == "Confirmada"
    # Y el motivo anterior ya no queda registrado
    assert asistencia["motivo"] is None
    assert "tengo turno en el trabajo" not in cliente.get(f"/eventos/{evento_id}").text


def test_hu03_el_integrante_intenta_cambiar_los_instrumentos_de_su_convocatoria(
    conexion, cliente
):
    # Dado que Pedro fue convocado con guitarra eléctrica y voz
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica", "voz"]})
    _como(cliente, conexion, "Pedro")

    # Cuando Pedro intenta reemplazar guitarra eléctrica por guitarra acústica
    respuesta = _responder(
        cliente,
        evento_id,
        "confirmar",
        instrumentos=[
            id_instrumento(conexion, "guitarra acústica"),
            id_instrumento(conexion, "voz"),
        ],
    )

    # Entonces los instrumentos de su convocatoria no cambian
    assert respuesta.status_code == 200
    assert _instrumentos_convocatoria(conexion, evento_id, "Pedro") == [
        "guitarra eléctrica",
        "voz",
    ]
    assert _asistencia(conexion, evento_id, "Pedro")["estado"] == "Pendiente"
    # Y Pedro es informado de que solo el Líder de Alabanza puede asignar los instrumentos
    assert "solo el Líder de Alabanza puede asignar los instrumentos" in respuesta.text


def test_hu03_el_integrante_intenta_confirmar_despues_de_que_el_evento_fue_cancelado(
    conexion, cliente
):
    # Dado que el evento fue cancelado (cancelar aún no está implementado: se prepara en la base)
    evento_id = _crear_evento(conexion, {"Pedro": ["bajo"]})
    conexion.execute(
        "UPDATE eventos_ensayo SET estado = 'Cancelado' WHERE id = ?", (evento_id,)
    )
    conexion.commit()
    _como(cliente, conexion, "Pedro")

    # Cuando Pedro intenta confirmar que asistirá
    respuesta = _responder(cliente, evento_id, "confirmar")

    # Entonces la asistencia de Pedro no queda registrada
    assert respuesta.status_code == 200
    assert _asistencia(conexion, evento_id, "Pedro")["estado"] == "Pendiente"
    # Y Pedro es informado de que la convocatoria ya no está disponible
    assert "la convocatoria ya no está disponible" in respuesta.text


def test_hu03_un_integrante_no_convocado_abre_el_evento(conexion, cliente):
    # Dado que el evento está vigente y Sofía no fue convocada
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica"]})
    _como(cliente, conexion, "Sofía")

    # Cuando Sofía abre el evento
    detalle = cliente.get(f"/eventos/{evento_id}")

    # Entonces Sofía ve la fecha del ensayo
    assert detalle.status_code == 200
    assert "2026-11-14" in detalle.text
    # Y no ve la opción de responder ni las respuestas de los convocados
    assert f'action="/eventos/{evento_id}/asistencia"' not in detalle.text
    assert "<th>Estado</th>" not in detalle.text


def test_hu03_un_integrante_no_convocado_intenta_confirmar_su_asistencia(
    conexion, cliente
):
    evento_id = _crear_evento(conexion, {"Pedro": ["guitarra eléctrica"]})
    _como(cliente, conexion, "Sofía")

    # Cuando Sofía intenta confirmar que asistirá
    respuesta = _responder(cliente, evento_id, "confirmar")

    # Entonces la asistencia de Sofía no queda registrada
    assert respuesta.status_code == 200
    assert _asistencia(conexion, evento_id, "Sofía") is None
    total = conexion.execute("SELECT COUNT(*) FROM asistencias").fetchone()[0]
    assert total == 1  # solo la asistencia Pendiente de Pedro
    # Y Sofía es informada de que no fue convocada a este evento
    assert "no fuiste convocado a este evento" in respuesta.text


def test_hu03_el_lider_revisa_el_estado_de_las_respuestas_de_los_convocados(
    conexion, cliente
):
    # Dado que Marta creó el evento convocando a Pedro, Ana y Luis
    evento_id = _crear_evento(
        conexion,
        {"Pedro": ["guitarra eléctrica"], "Ana": ["teclado"], "Luis": ["batería"]},
    )
    # Y que Pedro confirmó su asistencia
    _como(cliente, conexion, "Pedro")
    _responder(cliente, evento_id, "confirmar")
    # Y que Ana informó que no asistirá porque «tengo turno en el trabajo»
    _como(cliente, conexion, "Ana")
    _responder(cliente, evento_id, "no_asistire", motivo="tengo turno en el trabajo")
    # Y que Luis todavía no responde

    # Cuando Marta abre el detalle del evento
    _como(cliente, conexion, "Marta")
    detalle = cliente.get(f"/eventos/{evento_id}")
    texto = " ".join(detalle.text.split())

    # Entonces ve a cada convocado con su instrumento, su estado y el motivo de Ana
    assert detalle.status_code == 200
    assert '<td>Pedro</td> <td>guitarra eléctrica</td> <td><span class="badge">Confirmada</span></td>' in texto
    assert (
        '<td>Ana</td> <td>teclado</td> <td><span class="badge">No asiste</span></td> '
        "<td>tengo turno en el trabajo</td>"
    ) in texto
    assert '<td>Luis</td> <td>batería</td> <td><span class="badge">Pendiente</span></td>' in texto
