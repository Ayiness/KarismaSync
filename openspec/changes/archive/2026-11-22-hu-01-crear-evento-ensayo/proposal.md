# Proposal — HU-01 Crear evento de ensayo con roles requeridos

## Why

Hoy la convocatoria de ensayos se hace por WhatsApp o en reuniones informales, por lo que la fecha, el quórum y los roles requeridos se pierden entre mensajes y el líder no tiene un registro estructurado. HU-01 digitaliza esa convocatoria: el Líder de Alabanza crea el evento dentro de KarismaSync y la banda recibe la notificación.

## What Changes

- Se agrega una pantalla «Crear evento de ensayo» para el Líder de Alabanza, con fecha, quórum y roles requeridos.
- Se registra el evento en estado `Vigente` y se emite su `Convocatoria`.
- Se simula el envío de la convocatoria a todos los integrantes de la banda mediante un adaptador del Servicio de notificaciones.
- Se rechaza la creación si el usuario no es Líder de Alabanza, si no indica roles requeridos o si falta el quórum, sin registrar el evento ni enviar convocatorias.
- Se agregan datos de ejemplo (una banda con 6 integrantes, un líder y el catálogo de instrumentos) y una prueba automática por cada escenario Gherkin de HU-01.

## Capabilities

### New Capabilities
- `eventos-ensayo`: creación, convocatoria y ciclo de vida de los eventos de ensayo de la banda, incluida la validación de quién puede crearlos.

### Modified Capabilities
- Ninguna. No existen capacidades previas en `openspec/specs/`.

## Impact

- Código nuevo: aplicación FastAPI con plantillas Jinja2, dominio `EventoDeEnsayo`, `Convocatoria`, `Banda`, `Integrante` e `Instrumento`, migraciones SQLite y adaptador simulado del Servicio de notificaciones.
- Datos: `data/app.db` con migraciones en `app/db/migrations/` y seed idempotente.
- Pruebas: una prueba de integración por escenario Gherkin de HU-01 con pytest.
- Fuera de alcance: abrir la convocatoria desde la notificación (HU-02), registrar asistencia e instrumentos (HU-03), evaluar quórum y roles (HU-04), decidir esperar o reagendar (HU-05), cancelar o terminar eventos, autenticación real y requisitos no funcionales.
- Trazabilidad: HU-01, actividad TO-BE «Crear evento indicando fecha y roles requeridos», CU-01 «Crear convocatoria de ensayo», RF-01 y RF-02.
