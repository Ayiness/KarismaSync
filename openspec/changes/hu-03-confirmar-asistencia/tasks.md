# Tasks — HU-03 Confirmar asistencia al ensayo

## 1. Base de datos

- [ ] 1.1 Escribir `app/db/migrations/004_asistencias.sql` con la tabla `asistencias` y las asistencias `Pendiente` de las convocatorias existentes.
- [ ] 1.2 En `crear_evento`, insertar la asistencia `Pendiente` de cada convocatoria; verificar que las pruebas de HU-01 sigan pasando.

## 2. Dominio y servicio

- [ ] 2.1 Crear `app/dominio/asistencia.py` con `EstadoAsistencia`, `TRANSICIONES` (EST-02) y `transicionar`.
- [ ] 2.2 Crear `app/servicios/registrar_asistencia.py` con las validaciones y mensajes del diseño.

## 3. Rutas y pantallas

- [ ] 3.1 Agregar `POST /eventos/{id}/asistencia`.
- [ ] 3.2 Ampliar `GET /eventos/{id}` y `evento_detalle.html`: datos del convocado, formulario según el estado y tabla de respuestas para el líder y los convocados.

## 4. Pruebas (escenarios Gherkin de HU-03)

- [ ] 4.1 El integrante confirma su asistencia y ve los instrumentos asignados.
- [ ] 4.2 El integrante informa que no asistirá.
- [ ] 4.3 El integrante intenta informar que no asistirá sin indicar el motivo.
- [ ] 4.4 El integrante cambia su respuesta de confirmada a no asiste.
- [ ] 4.5 El integrante cambia su respuesta de no asiste a confirmada.
- [ ] 4.6 El integrante intenta cambiar los instrumentos de su convocatoria.
- [ ] 4.7 El integrante intenta confirmar después de que el evento fue cancelado.
- [ ] 4.8 Un integrante no convocado abre el evento.
- [ ] 4.9 Un integrante no convocado intenta confirmar su asistencia.
- [ ] 4.10 El líder revisa el estado de las respuestas de los convocados.
- [ ] 4.11 Pruebas de dominio de EST-02: una transición válida y una inválida.

## 5. Documentación

- [ ] 5.1 Actualizar `README.md`, `12-trazabilidad.md` (HU-03 → código → pruebas) y `.cin324/proyecto.md`.
