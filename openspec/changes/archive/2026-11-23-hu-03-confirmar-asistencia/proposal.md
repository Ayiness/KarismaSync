# Proposal — HU-03 Confirmar asistencia al ensayo

## Why

Hoy el líder crea el evento y los músicos reciben la convocatoria, pero no pueden responderla dentro del sistema: la asistencia se sigue preguntando por mensaje y el líder no sabe quién vendrá ni por qué alguien no puede. HU-03 permite que cada músico convocado confirme su asistencia o informe que no asistirá con un motivo, que pueda cambiar su respuesta mientras el evento esté vigente, y que el líder y los convocados vean el estado de cada respuesta.

## What Changes

- El detalle del evento muestra al músico convocado sus instrumentos asignados, el estado de su respuesta y el formulario para responder.
- El músico puede confirmar (queda `Confirmada` con los instrumentos de su convocatoria) o indicar que no asistirá con un motivo obligatorio de hasta 200 caracteres (queda `No asiste`).
- Mientras el evento esté vigente, puede cambiar su respuesta («Cambiar respuesta»): de `Confirmada` a `No asiste` (con motivo) o de `No asiste` a `Confirmada` (se borra el motivo).
- Se rechaza responder si el evento no está vigente, si el integrante no fue convocado, si falta el motivo o si se intenta cambiar los instrumentos.
- El líder y los convocados ven la tabla de convocados con instrumentos y estado; el motivo de inasistencia solo lo ven el líder y el propio integrante; un integrante no convocado ve el evento sin esa tabla.
- Cada convocatoria nace con su asistencia en `Pendiente` (transición `convocatoriaEmitida` de EST-02).

## Capabilities

### New Capabilities
- `asistencia-convocatoria`: responder la convocatoria de un evento y revisar las respuestas de los convocados.

### Modified Capabilities
- Ninguna en la spec: la creación del evento (HU-01) solo agrega internamente la asistencia `Pendiente` de cada convocatoria, sin cambiar sus escenarios.

## Impact

- Datos: migración `004_asistencias.sql` (tabla `asistencias`) y asistencias `Pendiente` para las convocatorias existentes.
- Código: `app/dominio/asistencia.py` (EST-02), `app/servicios/registrar_asistencia.py`, `app/servicios/crear_evento.py` (asistencia Pendiente al emitir), ruta `POST /eventos/{id}/asistencia` y `GET /eventos/{id}` en `app/rutas/eventos.py`, plantilla `evento_detalle.html`.
- Pruebas: una por escenario Gherkin de HU-03 en `tests/test_hu03_confirmar_asistencia.py` y pruebas de dominio de EST-02.
- Fuera de alcance: acceso desde la notificación con sus propios escenarios (HU-02), evaluación del quórum y confirmación del ensayo (HU-04), alertas (HU-05), cancelar o terminar eventos (`eventoCerrado`), requisitos no funcionales.
- Trazabilidad: HU-03 (CA1–CA9), actividad TO-BE «Confirmar asistencia al ensayo», CU-05 y CU-06, DSS-05 y DSS-06, EST-02, RF-04, RF-05, RF-06 y RF-14.
