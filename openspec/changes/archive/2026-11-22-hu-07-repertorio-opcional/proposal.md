# Proposal — HU-07 Incluir un repertorio opcional de canciones en el evento

## Why

No todos los eventos de la banda son ensayos: también hay reuniones de coordinación u otras actividades en las que no se interpretarán canciones. Hoy el repertorio se acuerda por mensajes separados y no queda asociado a la convocatoria. HU-07 permite incluir canciones de forma opcional al crear un evento, con el bloque de selección activado por defecto para los ensayos y la posibilidad de desactivarlo para los eventos que no lo necesitan.

## What Changes

- El formulario «Crear evento de ensayo» incorpora un bloque de repertorio activado por defecto, con el catálogo de canciones de la banda.
- El líder puede seleccionar cero o más canciones, o desactivar el bloque; el evento se crea igualmente sin canciones.
- KarismaSync registra únicamente las canciones seleccionadas y las asocia al evento.
- El detalle del evento muestra el repertorio registrado o indica que no incluye canciones.
- Se agregan 20 canciones de ejemplo y una prueba automática por cada escenario Gherkin de HU-07.

## Capabilities

### New Capabilities
- `repertorio-opcional`: selección opcional de canciones del catálogo al crear un evento y consulta del repertorio registrado.

### Modified Capabilities
- `eventos-ensayo`: la creación del evento acepta un repertorio opcional de canciones, sin cambiar su estado ni sus transiciones.

## Impact

- Código: migración `003_canciones.sql`, seed con 20 canciones, servicio de creación, rutas `GET /eventos/nuevo` y `POST /eventos`, y plantillas de formulario y detalle.
- Datos: tablas `canciones` y `eventos_canciones`; no se modifica el estado del evento.
- Pruebas: una prueba de integración por escenario Gherkin de HU-07 con pytest.
- Fuera de alcance: edición posterior del repertorio, reproducción de audio, letras, tonalidades y cualquier integración musical externa.
- Trazabilidad: HU-07, actividad TO-BE «Crear evento convocando músicos y asignando sus instrumentos (incluye el repertorio opcional de canciones)», CU-04 «Incluir repertorio opcional al crear un evento», RF-13 y DSS-04.
