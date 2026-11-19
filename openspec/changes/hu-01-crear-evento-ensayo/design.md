# Design — HU-01 Crear evento de ensayo con roles requeridos

## Context

La aplicación parte de cero: no hay código de servidor, base de datos ni plantillas. El stack acordado es Python 3.12 + FastAPI + Jinja2 + `sqlite3` estándar + pytest. La fuente de verdad son `08-modelo-dominio.md`, `11-diagramas-estado.md` (EST-01) y `diagramas/dss-01-crear-convocatoria.puml` (DSS-01). Ver `proposal.md` para la motivación.

## Goals / Non-Goals

**Goals:**
- Crear el esqueleto de la aplicación (FastAPI, plantillas, migraciones, seed y pruebas).
- Implementar el flujo completo de CU-01: formulario, validación de rol, registro del evento, emisión de convocatorias y notificación simulada.
- Dejar una única función de transición de estado para `EventoDeEnsayo`, reutilizable por HU-04 y HU-05.

**Non-Goals:**
- Asistencias, evaluación de quórum/roles, alertas, reagendamiento, cancelación o cierre del evento.
- Autenticación real, requisitos no funcionales y envío real de notificaciones.
- Pantallas de historial, edición o borrado de eventos.

## Decisions

### Modelo de datos (derivado del modelo de dominio)

| Tabla | Columnas | Origen y reglas |
|-------|----------|-----------------|
| `bandas` | `id`, `nombre` | Clase `Banda` (`nombre`). |
| `integrantes` | `id`, `nombre`, `banda_id`, `es_lider` | Clase `Integrante` (`nombre`); `banda_id` por `integra` (1..*–1, `NOT NULL`); `es_lider` representa el extremo «líder» de `lidera` (rol, no clase). |
| `instrumentos` | `id`, `nombre UNIQUE`, `es_musico_base` | Clase `Instrumento` (`nombre`, `esMusicoBase`). |
| `eventos_ensayo` | `id`, `banda_id`, `fecha`, `quorum`, `estado` | Clase `EventoDeEnsayo` (`fecha`, `quorum`, `estado`); `banda_id` por `organiza` (1–0..*). `estado` con `CHECK` en `Vigente`, `Confirmado`, `Cancelado`, `Terminado`. |
| `eventos_requieren_instrumentos` | `evento_id`, `instrumento_id` | Asociación muchos a muchos `requiere` (`rolesRequeridos`), con claves foráneas y `ON DELETE CASCADE` desde el evento (composición). |
| `convocatorias` | `id`, `evento_id`, `integrante_id`, `fecha_ensayo`, `fecha_envio` | Clase `Convocatoria` (`fechaEnsayo`, `fechaEnvio`); una fila por destinatario, `ON DELETE CASCADE` desde el evento (composición) y referencia al integrante (`es recibida por`). |
| `integraciones_log` | `id`, `sistema`, `mensaje`, `detalle`, `fecha` | Registro de la integración simulada; no es clase del dominio. |

`Alerta` y `Asistencia` no se crean todavía: pertenecen a HU-03, HU-04 y HU-05.

### Transición de estado (derivada de EST-01)

Una sola función `transicionar(evento, evento_estado)` en `app/dominio/evento_ensayo.py` valida el estado actual y aplica la transición; una transición no permitida lanza un error de dominio con mensaje claro. Para HU-01:

| Estado origen | Evento | Guarda | Acción | Estado destino |
|---------------|--------|--------|--------|----------------|
| Inicial (sin fila) | `crearEvento` | Líder autorizado; fecha válida, quórum ≥ 1 y al menos un rol | Insertar evento, emitir convocatorias y solicitar notificación | `Vigente` |

### Rutas (derivadas de DSS-01)

| Método y ruta | Mensaje de DSS-01 | Pantalla / resultado |
|---------------|-------------------|----------------------|
| `GET /` | — | Inicio con selector de usuario de demostración y lista de eventos. |
| `POST /demo/usuario` | — | Guarda en cookie `usuario_id` el usuario de demostración elegido. |
| `GET /eventos/nuevo` | — | Formulario «Crear evento de ensayo» (fecha, quórum, roles). |
| `POST /eventos` | `crearEvento(fecha, rolesRequeridos)` | Valida y registra; redirige a `GET /eventos/{id}`. |
| `GET /eventos/{id}` | `eventoCreado(evento, envioSolicitado)` | Detalle del evento y confirmación visible para el líder. |

Las ramas `alt` de DSS-01 se implementan como validaciones antes de registrar: usuario sin rol de líder, sin roles requeridos o sin quórum. En los tres casos se vuelve al formulario con el mensaje de error correspondiente y no se inserta nada.

### Integración externa simulada

- Interfaz `ServicioNotificaciones` con `enviar_convocatoria(destinatarios, evento, enlace) -> RespuestaEnvio`.
- `ServicioNotificacionesSimulado` registra la solicitud en `integraciones_log`, devuelve `solicitudAceptada` y registra una entrega por destinatario. Se selecciona con la variable `NOTIFICACIONES_MODO=simulado` (valor por defecto).
- El enlace de la convocatoria apunta a `GET /eventos/{id}`; abrirlo desde la notificación será HU-02.

### Rol de demostración

No hay autenticación. Un selector en la plantilla base elige entre los integrantes sembrados y guarda `usuario_id` en una cookie. La capa de servicio recibe el integrante y comprueba `es_lider`; las pruebas envían la cookie directamente. Alternativa considerada: pasar el usuario por query string, pero la cookie evita repetirlo en cada enlace y mantiene las rutas limpias.

### Validaciones

- Rol: `es_lider = 1`; mensaje «solo el Líder de Alabanza puede crear eventos de ensayo».
- Roles requeridos: al menos un `instrumento_id` válido; mensaje «debe indicar al menos un rol requerido».
- Quórum: entero ≥ 1; mensaje «debe indicar el quórum requerido».
- Fecha: obligatoria y parseable como fecha ISO (`YYYY-MM-DD`); no se restringe que sea pasada porque los artefactos no lo piden.

### Pruebas

Una prueba de integración por escenario de `specs/eventos-ensayo/spec.md`, nombradas «HU-01 · …», con una base SQLite temporal por prueba y el servicio de notificaciones simulado. Las aserciones revisan la base (evento, convocatorias, log de integración) y los mensajes visibles.

## Risks / Trade-offs

- [La cookie de demostración no es autenticación real] → Es una decisión del taller; se documenta en el README y no se confunde con seguridad.
- [La tabla `convocatorias` mezcla el aviso con su destinatario] → Simplifica HU-01 y permite consultar destinatarios; si HU-02 necesita un enlace único por integrante, se agrega una columna con una migración nueva.
- [Validar la fecha solo como ISO permite fechas pasadas] → Se acepta porque ningún artefacto lo prohíbe; si el estudiante lo pide, se cambia con `cin324-validar-sistema` y una nueva historia/ajuste.
- [La entrega simulada siempre es exitosa] → RNF-04 no se implementa; el log deja evidencia de lo solicitado y entregado.

## Migration Plan

1. Migración `001_esquema_inicial.sql` crea las tablas y `schema_migrations`.
2. `python -m app.db.seed` inserta la banda, 6 integrantes (Marta como líder, Pedro, Ana, Luis, Sofía y Diego), los instrumentos (batería, bajo, guitarra, teclado, voz) y deja todo idempotente.
3. No hay datos previos que migrar; el rollback consiste en borrar `data/app.db` y volver a ejecutar el seed.
