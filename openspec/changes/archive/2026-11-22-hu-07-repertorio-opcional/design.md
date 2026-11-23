# Design — HU-07 Incluir un repertorio opcional de canciones en el evento

## Context

La aplicación ya crea eventos de ensayo con fecha, quórum, convocados e instrumentos (HU-01). La fuente de verdad para esta historia es `08-modelo-dominio.md` (clase `Cancion` y asociación `incluye`), `04-historias-usuario.md` (HU-07), `07-criterios-aceptacion.md` (HU-07) y `09-casos-uso.md` (CU-04). El repertorio es un dato opcional del evento y no modifica el ciclo de vida de EST-01.

## Goals / Non-Goals

**Goals:**
- Permitir crear un evento con cero o más canciones del catálogo.
- Mostrar el bloque de repertorio activado por defecto y permitir desactivarlo.
- Registrar solo las canciones seleccionadas y mostrarlas en el detalle.
- Sembrar 20 canciones de ejemplo.

**Non-Goals:**
- Agregar, editar o quitar canciones después de crear el evento.
- Modelar letras, tonalidades, duración, archivos de audio o derechos de autor.
- Agregar estados o transiciones al evento.
- Implementar requisitos no funcionales.

## Decisions

### Modelo de datos (derivado del modelo de dominio)

| Tabla | Columnas | Origen y reglas |
|-------|----------|-----------------|
| `canciones` | `id`, `titulo UNIQUE`, `autor` | Clase `Cancion` (`titulo`, `autor`). Catálogo de la banda. |
| `eventos_canciones` | `evento_id`, `cancion_id` | Asociación `incluye` (`repertorio`) con 0..* en ambos extremos. Claves foráneas y `ON DELETE CASCADE` desde el evento (composición); `ON DELETE RESTRICT` desde la canción. |

No se agrega un atributo `incluyeRepertorio` a `eventos_ensayo`: el evento sin filas en `eventos_canciones` representa un evento sin repertorio. El bloque activado por defecto es una decisión de interfaz (parámetro `incluir_repertorio` del formulario), no un estado del dominio.

### Rutas (derivadas de CU-04 y DSS-04)

| Método y ruta | Mensaje de DSS-04 | Pantalla / resultado |
|---------------|-------------------|----------------------|
| `GET /eventos/nuevo` | `formularioEvento(catalogoCanciones, repertorioActivoPorDefecto)` | Formulario con el bloque de repertorio activado y las 20 canciones del catálogo. |
| `POST /eventos` | `crearEvento(fecha, quorum, convocados, canciones[])` | Valida, registra el evento y las canciones seleccionadas; redirige al detalle. |
| `GET /eventos/{id}` | `eventoCreado(evento, repertorioRegistrado)` | Detalle con el repertorio o el aviso de que no incluye canciones. |

### Validaciones

- Cada canción enviada debe existir en el catálogo; si no, se vuelve al formulario con un error y no se registra nada.
- La lista de canciones se deduplica.
- Si el bloque de repertorio está desactivado, se ignoran las canciones enviadas y el evento se crea sin repertorio.
- Un evento con el bloque activo y sin canciones es válido: la selección no es obligatoria.
- El repertorio no altera las validaciones existentes de fecha, quórum, convocados e instrumentos.

### Pruebas

Una prueba de integración por escenario de `specs/repertorio-opcional/spec.md`, con una base SQLite temporal por prueba y el servicio de notificaciones simulado. Las aserciones revisan la base (`eventos_canciones`), el catálogo y los textos visibles del formulario y del detalle.

## Risks / Trade-offs

- [No se guarda si el líder desactivó el bloque o simplemente no seleccionó canciones] → Ambos casos producen el mismo resultado de negocio: un evento sin repertorio. Si más adelante se necesita distinguirlos, se agrega una columna con una migración nueva.
- [El catálogo es global para la banda sembrada] → Es suficiente para el alcance del taller; no se modela multibanda por canción.
- [No se puede editar el repertorio después de crear el evento] → Queda fuera de HU-07; se puede agregar como una historia posterior.

## Migration Plan

1. La migración `003_canciones.sql` crea `canciones` y `eventos_canciones`.
2. `python -m app.db.seed` inserta 20 canciones de ejemplo de forma idempotente.
3. No hay datos previos que migrar: los eventos existentes quedan sin repertorio.
4. Rollback: borrar `data/app.db` y volver a ejecutar el seed (los datos de ejemplo se reconstruyen).
