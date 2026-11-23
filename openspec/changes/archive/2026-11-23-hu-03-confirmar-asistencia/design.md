# Design — HU-03 Confirmar asistencia al ensayo

## Context

Fuentes: HU-03 en `04-historias-usuario.md` (CA1–CA9) y `07-criterios-aceptacion.md` (10 escenarios), clase `Asistencia`, enumeración `EstadoAsistencia` y asociación `tiene` en `08-modelo-dominio.md`, EST-02 en `11-diagramas-estado.md`, CU-05 y CU-06 en `09-casos-uso.md`, DSS-05 y DSS-06 en `10-diagramas-secuencia.md`. Decisiones del equipo (2026-11-23): el músico puede cambiar su respuesta mientras el evento esté vigente; el líder y los convocados ven los estados, pero el motivo de inasistencia es privado y solo lo ven el líder y el propio integrante (corrección del 2026-11-23 sobre la decisión inicial); un no convocado ve el evento pero no puede responder ni ver las respuestas; el motivo es obligatorio y de hasta 200 caracteres.

## Goals / Non-Goals

**Goals:** responder la convocatoria (confirmar, no asistir con motivo, cambiar la respuesta), mostrar los instrumentos asignados y mostrar el estado de las respuestas a quienes corresponde.

**Non-Goals:** escenarios propios de HU-02, evaluación del quórum (HU-04), alertas (HU-05), cancelar o terminar eventos, notificaciones por la respuesta.

## Decisions

### Modelo de datos (derivado del modelo de dominio)

| Tabla | Columnas | Origen y reglas |
|-------|----------|-----------------|
| `asistencias` | `id`, `convocatoria_id UNIQUE`, `estado`, `motivo`, `fecha_respuesta` | Clase `Asistencia` y asociación `tiene` (Convocatoria 1 – 1 Asistencia, composición: `ON DELETE CASCADE`). `estado` con `CHECK` en `Pendiente`, `Confirmada`, `No asiste`, `Sin respuesta`. `CHECK` para que `motivo` exista (1–200 caracteres) solo cuando `estado = 'No asiste'`. |

Los instrumentos de la asistencia no se copian: son los de `convocatorias_instrumentos` (asociación `asigna`). La migración crea una asistencia `Pendiente` para cada convocatoria existente.

### Estados y transiciones (EST-02, `app/dominio/asistencia.py`)

`EstadoAsistencia` = `Pendiente`, `Confirmada`, `No asiste`, `Sin respuesta`. Tabla `TRANSICIONES` con el mismo patrón que `evento_ensayo.py`:

| Origen | Evento | Guarda | Destino |
|--------|--------|--------|---------|
| Inicial | `convocatoriaEmitida` | — | Pendiente |
| Pendiente | `registrarAsistencia` | confirma | Confirmada |
| Pendiente | `registrarAsistencia` | no asistirá e indica motivo | No asiste |
| Confirmada | `registrarAsistencia` | no asistirá e indica motivo | No asiste |
| No asiste | `registrarAsistencia` | confirma | Confirmada |
| Pendiente | `eventoCerrado` | — | Sin respuesta |

La tabla se indexa por `(estado origen, evento, asiste)`, donde `asiste` es `True` (confirma) o `False` (no asistirá); para `convocatoriaEmitida` y `eventoCerrado` vale `None`. Cualquier combinación no modelada (por ejemplo `Confirmada` + `registrarAsistencia` con `asiste=True`, o cualquier respuesta desde `Sin respuesta`) lanza `ErrorTransicion` con el mensaje «ya registraste esa respuesta». La guarda «evento vigente» y la de «indica motivo» se validan en el servicio antes de transicionar.

### Servicio `registrar_asistencia(conexion, usuario_id, evento_id, asiste, motivo, instrumentos_ids=None)`

Validaciones en este orden, sin modificar nada si falla alguna (mensajes exactos):

1. Usuario de demostración no elegido → «seleccione un usuario de demostración».
2. Evento inexistente → 404 en la ruta.
3. Integrante no convocado → «no fuiste convocado a este evento» (`noConvocado`).
4. Evento distinto de `Vigente` → «la convocatoria ya no está disponible» (`convocatoriaNoDisponible`).
5. Se enviaron instrumentos → «solo el Líder de Alabanza puede asignar los instrumentos» (`instrumentosAsignadosPorLider`).
6. No asiste y motivo vacío o solo espacios → «debe indicar el motivo por el que no asistirá» (`sinMotivo`); más de 200 caracteres → «el motivo no puede superar los 200 caracteres».
7. Transición no modelada en EST-02 → mensaje de `ErrorTransicion` («ya registraste esa respuesta»).

Si todo es válido: `Confirmada` guarda `motivo = NULL`; `No asiste` guarda el motivo recortado; ambos guardan `fecha_respuesta`.

### Rutas (derivadas de DSS-05 y DSS-06)

| Método y ruta | Mensaje | Resultado |
|---------------|---------|-----------|
| `GET /eventos/{id}` | `verEvento(evento)` → `detalleEvento(...)` / `estadoConvocados(...)` | Para un convocado: sus instrumentos, su estado y el formulario si el evento está vigente. Para el líder: tabla con integrante, instrumentos, estado y motivo. Para los convocados: la misma tabla sin la columna de motivo (su propio motivo aparece en «Tu convocatoria»). Para un no convocado: el evento sin formulario ni tabla. |
| `POST /eventos/{id}/asistencia` | `registrarAsistencia(evento, asiste, motivo)` | Éxito → redirige a `GET /eventos/{id}` (`respuestaRegistrada`). Error → vuelve a mostrar el detalle con el mensaje (`respuestaRechazada`). |

Formulario: si el estado es `Pendiente`, dos opciones («Confirmar asistencia» y «No asistiré» con campo de motivo). Si es `Confirmada`, solo «Cambiar respuesta: no asistiré» con motivo. Si es `No asiste`, se muestra el motivo y «Cambiar respuesta: confirmar asistencia».

### HU-01

`crear_evento` inserta la asistencia `Pendiente` de cada convocatoria en la misma transacción (`convocatoriaEmitida`). Sus pruebas no cambian.

### Pruebas

Una prueba de integración por escenario de `specs/asistencia-convocatoria/spec.md` (prefijo `test_hu03_`), con base SQLite temporal, y pruebas de dominio con una transición válida y una inválida de EST-02.

## Risks / Trade-offs

- [No existe todavía cancelar ni terminar eventos] → Para el escenario del evento cancelado, la prueba cambia `eventos_ensayo.estado` a `Cancelado` directamente en la base de prueba. `eventoCerrado` queda modelado pero no implementado.
- [«Su respuesta queda considerada en la evaluación del quórum» (escenario 1)] → HU-04 no está implementada; se cumple dejando la asistencia `Confirmada` guardada y consultable junto con los instrumentos de la convocatoria.
- [Sin autenticación real] → El integrante se identifica con el selector de demostración.

## Migration Plan

1. `004_asistencias.sql` crea la tabla y las asistencias `Pendiente` de las convocatorias existentes.
2. `python -m app.db.seed` no cambia (no siembra eventos).
3. Rollback: borrar `data/app.db` y volver a ejecutar el seed.
