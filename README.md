# KarismaSync

Aplicación web para organizar las convocatorias de ensayo de la banda.
Generada historia por historia desde la documentación de Ingeniería de Requisitos.
Historias implementadas:

| Historia | Cambio de OpenSpec | Pruebas |
|----------|--------------------|---------|
| HU-01 — Crear evento de ensayo convocando músicos con sus instrumentos | `hu-01-crear-evento-ensayo` | `tests/test_hu01_crear_evento.py` |
| HU-06 — Registrar el perfil instrumental del integrante | `hu-06-perfil-instrumental` | `tests/test_hu06_perfil_instrumental.py` |
| HU-07 — Incluir un repertorio opcional de canciones en el evento | `hu-07-repertorio-opcional` | `tests/test_hu07_repertorio.py` |

La trazabilidad completa (historia → código → prueba) está en [`12-trazabilidad.md`](./12-trazabilidad.md).

> El Servicio de notificaciones está **simulado**: no se envía correo ni mensaje real.
> Cada solicitud y cada entrega quedan registradas en la tabla `integraciones_log`.
> Tampoco hay autenticación real: se usa un selector de usuario de demostración.

## Requisitos

- Python 3.12 o superior.

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

En macOS o Linux, activa el entorno con `source .venv/bin/activate`.

## Crear la base de datos y los datos de ejemplo

```powershell
python -m app.db.seed
```

Crea `data/app.db`, aplica las migraciones de `app/db/migrations/` y siembra:

- Banda **KarismaSync** con 6 integrantes: Marta (Líder de Alabanza), Pedro, Ana, Luis, Sofía y Diego.
- Catálogo de instrumentos: batería, bajo, guitarra eléctrica, guitarra acústica, teclado y voz.
- Perfil instrumental de ejemplo: Marta (voz), Pedro (guitarra eléctrica), Ana (teclado), Luis (batería), Sofía (bajo) y Diego (guitarra acústica).
- Catálogo de 20 canciones de ejemplo para el repertorio opcional de los eventos.

El comando es idempotente: ejecutarlo otra vez no duplica datos.

## Ejecutar

```powershell
uvicorn app.main:app --reload
```

Abre <http://localhost:8000>.

## Repertorio opcional de canciones

Al crear un evento, el bloque **Repertorio de canciones (opcional)** aparece activado por defecto.
El líder puede seleccionar una o varias canciones del catálogo, dejar la selección vacía o
desactivar el bloque; en todos los casos el evento se crea. Si no hay canciones, el detalle
indica que el evento no incluye repertorio. Las canciones no seleccionadas no se asocian.

## Probar

```powershell
pytest
```

Las pruebas cubren los escenarios Gherkin de HU-01, HU-06 y HU-07 (una prueba por escenario, con el
prefijo `test_hu0X_`), la transición de estado del evento, la integración simulada de notificaciones y las pantallas.
Las pruebas crean su propia base SQLite temporal; no necesitan ejecutar el seed antes.

## Estructura

| Ruta | Contenido |
|------|-----------|
| `app/db/` | Conexión SQLite, migraciones y datos de ejemplo |
| `app/dominio/` | `EventoDeEnsayo` y sus transiciones de estado (EST-01) |
| `app/servicios/` | Lógica de creación del evento y validaciones |
| `app/integraciones/` | Adaptador simulado del Servicio de notificaciones |
| `app/rutas/` | Rutas HTTP |
| `app/templates/` | Pantallas Jinja2 |
| `tests/` | Pruebas automáticas |
| `openspec/` | Cambios de OpenSpec por historia (`changes/`, archivados en `changes/archive/`) y especificaciones vigentes (`specs/`) |
| `diagramas/` | Fuentes (`.puml`, `.drawio`, `.bpmn`) y PNG de los diagramas |
| `eval2/` | Evaluación 2: `CAMBIOS.md` con el cambio de requerimientos por artefacto |
