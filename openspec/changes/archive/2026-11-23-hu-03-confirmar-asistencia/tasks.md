# Tasks — HU-03 Confirmar asistencia al ensayo

## 1. Base de datos

- [x] 1.1 Escribir `app/db/migrations/004_asistencias.sql` con la tabla `asistencias` y las asistencias `Pendiente` de las convocatorias existentes.
- [x] 1.2 En `crear_evento`, insertar la asistencia `Pendiente` de cada convocatoria; verificar que las pruebas de HU-01 sigan pasando.

## 2. Dominio y servicio

- [x] 2.1 Crear `app/dominio/asistencia.py` con `EstadoAsistencia`, `TRANSICIONES` (EST-02) y `transicionar`.
- [x] 2.2 Crear `app/servicios/registrar_asistencia.py` con las validaciones y mensajes del diseño.

## 3. Rutas y pantallas

- [x] 3.1 Agregar `POST /eventos/{id}/asistencia`.
- [x] 3.2 Ampliar `GET /eventos/{id}` y `evento_detalle.html`: datos del convocado, formulario según el estado y tabla de respuestas para el líder y los convocados.

## 4. Pruebas (escenarios Gherkin de HU-03)

- [x] 4.1 El integrante confirma su asistencia y ve los instrumentos asignados.
- [x] 4.2 El integrante informa que no asistirá.
- [x] 4.3 El integrante intenta informar que no asistirá sin indicar el motivo.
- [x] 4.4 El integrante cambia su respuesta de confirmada a no asiste.
- [x] 4.5 El integrante cambia su respuesta de no asiste a confirmada.
- [x] 4.6 El integrante intenta cambiar los instrumentos de su convocatoria.
- [x] 4.7 El integrante intenta confirmar después de que el evento fue cancelado.
- [x] 4.8 Un integrante no convocado abre el evento.
- [x] 4.9 Un integrante no convocado intenta confirmar su asistencia.
- [x] 4.10 El líder revisa el estado de las respuestas de los convocados.
- [x] 4.11 Pruebas de dominio de EST-02: una transición válida y una inválida.
- [x] 4.12 Un músico convocado revisa las respuestas sin ver los motivos de los demás.

## 5. Documentación

- [x] 5.1 Actualizar `README.md`, `12-trazabilidad.md` (HU-03 → código → pruebas) y `.cin324/proyecto.md`.
