# KarismaSync

Aplicación web para organizar las convocatorias de ensayo de la banda.
Generada historia por historia desde la documentación de Ingeniería de Requisitos.
Historias implementadas:

| Historia | Cambio de OpenSpec | Pruebas |
|----------|--------------------|---------|
| HU-01 — Crear evento de ensayo convocando músicos con sus instrumentos | `hu-01-crear-evento-ensayo` | `tests/test_hu01_crear_evento.py` |
| HU-06 — Registrar el perfil instrumental del integrante | `hu-06-perfil-instrumental` | `tests/test_hu06_perfil_instrumental.py` |
| HU-07 — Incluir un repertorio opcional de canciones en el evento | `hu-07-repertorio-opcional` | `tests/test_hu07_repertorio.py` |
| HU-03 — Confirmar asistencia al ensayo | `hu-03-confirmar-asistencia` | `tests/test_hu03_confirmar_asistencia.py`, `tests/test_asistencia_dominio.py` |

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

- Banda **KarismaSync** con 7 integrantes: Marta (Líder de Alabanza), Andrés (Representante de músicos), Pedro, Ana, Luis, Sofía y Diego (músicos).
- Catálogo de instrumentos: batería, bajo, guitarra eléctrica, guitarra acústica, teclado y voz.
- Perfil instrumental de ejemplo: Marta (voz), Pedro (guitarra eléctrica), Ana (teclado), Luis (batería), Sofía (bajo), Diego (guitarra acústica) y Andrés (voz).
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

## Responder una convocatoria (HU-03)

1. Elige a Marta en el selector y crea un evento convocando, por ejemplo, a Pedro, Ana y Luis.
2. Elige a Pedro y abre el evento desde el inicio: verás tus instrumentos, tu respuesta (`Pendiente`) y las opciones
   **Confirmar asistencia** o **No asistiré** (con motivo obligatorio, máximo 200 caracteres).
3. Mientras el evento esté `Vigente` puedes **cambiar tu respuesta**; al volver a confirmar se borra el motivo anterior.
4. La Líder de Alabanza ve la tabla con el estado (`Pendiente`, `Confirmada`, `No asiste`) y el motivo de cada convocado.
   Los demás convocados ven la tabla con los estados, pero no los motivos (son privados). Un integrante no convocado
   ve el evento, pero no puede responder ni ver las respuestas.

## Evento masivo y Representante de músicos (HU-08, HU-09)

1. Elige a Marta y crea un evento con el tipo **Evento masivo**. Queda `Pendiente de aprobación`:
   no se publica, los convocados no lo ven y no pueden responder. Se envía la solicitud de revisión a Andrés.
2. Elige a Andrés: en el inicio aparece **Convocatorias por revisar** (`/revisiones`), solo con los eventos
   masivos pendientes de su banda. Al abrir el evento ve la fecha, el quórum, los convocados y el repertorio.
3. **Aprobar convocatoria:** el evento queda `Vigente`, nacen las asistencias `Pendiente`, se notifica a los
   convocados y a la líder. **Rechazar convocatoria:** exige una justificación (máximo 200 caracteres); el evento
   queda `Rechazado`, no se notifica a los convocados y Marta ve la justificación en el detalle.
4. Andrés no puede crear eventos y Marta no puede aprobar su propio evento masivo. Un evento ya revisado o de tipo
   Ensayo no se puede revisar. Los ensayos siguen el flujo de HU-01, sin revisión.

El rol de cada integrante está en `integrantes.rol` (`Músico`, `Líder de Alabanza` o `Representante de músicos`),
y la migración `005_evento_masivo.sql` convierte el antiguo `es_lider`. Hay como máximo un representante por banda.

## Probar

```powershell
pytest
```

Las pruebas cubren los escenarios Gherkin de HU-01, HU-03, HU-06, HU-07, HU-08 y HU-09 (una prueba por escenario, con el
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
