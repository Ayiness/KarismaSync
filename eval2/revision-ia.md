# Evaluación 2 — Revisión de la IA sobre los cambios propuestos (24/11)

Cambio pedido por el profesor: (1) nuevo tipo de evento **Evento masivo**; (2) nuevo rol **Representante de músicos**, sin permisos de líder, que solo revisa las convocatorias de eventos masivos creadas por el líder y las confirma.

Se revisaron `evaluacion2.md`, HU-08/HU-09 y las fotos de los commits del martes 24/11 (`05952c5`, `be048b5`, `b4e11a0`, `abb01c8`, `3ea6214`).

## Qué estaba bien

| Propuesta | Por qué es correcta |
|---|---|
| Agregar un **tipo** al evento (foto del modelo: `tipo_ensayo`) | Es la forma mínima de distinguir un evento masivo sin crear otra clase. |
| Diferenciar el rol del integrante (foto: `tipo_integrante`) | El representante es un integrante más con un permiso distinto, igual que el líder. |
| HU-08: el evento masivo se envía primero al representante **sin publicarlo**, y este lo acepta o rechaza **con justificación** | Es exactamente la regla del cambio; quedó como CA3–CA5 de HU-08 y como el estado «Pendiente de aprobación». |
| Estado: la aprobación del representante ocurre **antes** de «Convocatoria abierta» y depende del **tipo de evento** | Es el orden correcto del ciclo de vida. |
| DSS: el representante como actor, la aprobación antes de `enviarConvocatoria` y reutilizar el servicio de notificaciones con su `loop` | Coincide con DSS-01 + DSS-07. |
| Identificar que había que tocar casos de uso, estados, secuencias e historias | Son artefactos afectados. |

## En qué se equivocaron

### Modelo de dominio (foto)
1. **`id_integrante` (y un id en ensayo) no van en un modelo de dominio.** El modelo de dominio es conceptual: muestra conceptos y atributos del negocio. La identidad de cada objeto es implícita; los `id` son una decisión de la base de datos, que **ya existe**: cada tabla tiene `id INTEGER PRIMARY KEY AUTOINCREMENT` (`integrantes`, `eventos_ensayo`, `convocatorias`, etc.). Por eso `Integrante` solo tiene `nombre`. Solo se modela un identificador cuando el negocio lo usa (por ejemplo, un RUT o un código de evento que la gente cita). Además, `id: string` no coincide con la base, que usa enteros.
2. **`tipo_integrante: string` no es la mejor forma.** El modelo ya representa al Líder como **rol** (asociación `lidera`), no como texto. El representante se modeló igual (`representa`). Con un string se pierde a qué banda representa y la regla «el representante no puede ser líder de la misma banda» (si no, el líder aprobaría sus propios eventos).
3. **`tipo_ensayo` como booleano (según «Pendiente a confirmación») o string.** Lo correcto es una enumeración `tipo : TipoEvento {Ensayo, Masivo}`: se lee mejor y admite otros tipos. El nombre «tipo de ensayo» también confunde, porque un evento masivo no es un ensayo.
4. **Faltó la revisión del representante.** Aprobar o rechazar con justificación es información del negocio: quién decidió, qué decidió, cuándo y por qué. Se agregó `RevisionDeEvento` (0..1 por evento, solo masivos) y los estados `Pendiente de aprobación` y `Rechazado` en `EstadoEvento`.
5. Detalles de notación: `snake_case` y `string` no siguen la convención del modelo (`camelCase`, tipos `Texto`, `Fecha`, `Entero`).

### Diagrama de estado (foto)
1. **«Representante de músico aprueba» no es un estado, es un evento.** Un estado describe una situación que dura («Pendiente de aprobación»); la acción del representante es la transición `aprobarEvento`.
2. **Lo pusieron dentro de Vigente.** Un evento que todavía no está aprobado no está publicado y los integrantes no pueden responder (RF-04 exige un evento vigente). Debe ir **fuera** de Vigente.
3. Faltaron la **decisión por tipo** (guardas `[tipo = Ensayo]` / `[tipo = Masivo]`; un ensayo normal no pasa por revisión), el **rechazo** (estado final `Rechazado`) y el evento en la línea entre la aprobación y «Convocatoria abierta».
4. En `evaluacion2.md`, «agregando la participación del representante» al diagrama de estado: un diagrama de estado no tiene participantes; el representante solo aparece como quien dispara la transición (guarda «representante de la banda»).

### Diagrama de secuencia (foto)
1. **La nota «registra y publica evento» antes de la aprobación** contradice HU-08 CA1 (no se publica sin aprobación). El evento se registra **Pendiente de aprobación** y no se publica.
2. **En un DSS el sistema no puede pedirle algo a un actor humano y esperar su respuesta dentro de la misma operación.** La aprobación es otro evento del sistema, iniciado por el representante cuando él revisa (puede ser horas después). Por eso quedan dos secuencias: DSS-01 termina con `eventoEnRevision` al líder y DSS-07 empieza con `verEventosPorRevisar()` del representante. Con su versión, el líder recibía «evento creado» recién después de la aprobación.
3. Faltaron los bloques `alt` para el rechazo con justificación, el rechazo sin justificación, el permiso (solo el representante revisa; el representante no crea eventos) y el caso de tipo Ensayo.
4. Mensajes sin parámetros (`crearEvento(tipo, fecha, quorum, convocados…)`), participante genérico «Sistemas externos» (es el «Servicio de notificaciones») y un `loop` vacío.
5. La foto subida a `09-casos-uso.md` era la misma foto del diagrama de secuencia (archivos idénticos), por eso la borraron. **No hubo propuesta de diagrama de casos de uso.**

### `evaluacion2.md` e historias
1. «CAMBIO 1 — ubicar un nuevo rol … **y atributos**» en el diagrama de casos de uso: los casos de uso no tienen atributos. Lo que cambia es un **actor nuevo**, un **caso de uso nuevo** (CU-07) y CU-01, que ahora recibe el tipo de evento.
2. Faltaron artefactos en la lista: **modelo de dominio** (sí lo dibujaron, pero no está en «CAMBIOS»), **requisitos** (RF-15, RF-16, RNF-01, RD-01), **criterios Gherkin** (07) y **trazabilidad** (12).
3. HU-08: errores de tipeo («Comfirmar», sin tildes), formato de lista (`-CA1` sin espacio) y criterios incompletos (justificación obligatoria, solo eventos masivos, sin permisos de líder, qué pasa al aprobar o rechazar). HU-09 estaba «pendiente…». Ambas se completaron.

### «Pendiente a confirmación»: qué significa
La nota dice: *«Revisar cómo está creada la base de datos para ver cambios en el modelo de dominio (cómo diferencia los roles), y agregar en la tabla evento de ensayo un nuevo tipo de ensayo que sea un booleano»*. Es decir, quedaron con dos tareas sin cerrar: (a) ver cómo la base distingue los roles para decidir cómo agregar el representante y (b) agregar a `eventos_ensayo` una columna booleana para el evento masivo.

- **(a) Respuesta:** la base distingue el rol con una columna booleana `integrantes.es_lider` (0/1). No existe un campo de rol general.
- **(b) Recomendación:** en `eventos_ensayo` conviene `tipo TEXT NOT NULL DEFAULT 'Ensayo' CHECK (tipo IN ('Ensayo','Masivo'))` en lugar de un booleano, y ampliar el `CHECK` de `estado` con `'Pendiente de aprobación'` y `'Rechazado'`. Para el rol, lo mínimo es una columna `es_representante` análoga a `es_lider`, o una tabla o columna de rol si quieren más roles después. También hará falta una tabla de revisiones (`evento_id`, `representante_id`, `decision`, `justificacion`, `fecha`).
- **Ojo con la dirección:** el modelo de dominio no se deriva de la base de datos; la base se diseña a partir del modelo. Revisar la base sirve para ver qué cambiar el jueves al implementar, no para decidir el modelo.

## Errores previos corregidos de paso
- `es recibida por` (Convocatoria – Integrante) decía `0..* a 1..*`, pero cada convocatoria es de **un** integrante (tiene una sola Asistencia y la tabla `convocatorias` tiene `integrante_id`). Quedó `0..* a 1`.
- `toca` decía `1 a 0..1`, pero el mismo texto dice que «un instrumento puede ser principal de muchos integrantes». Quedó `0..* a 0..1`.

## Preguntas para validar con el profesor
- Si un evento masivo **reagendado** (HU-05) debe volver a revisión.
- Si un evento rechazado puede corregirse y reenviarse, o si el líder crea uno nuevo (se modeló lo segundo).
- Si el representante debe ser integrante de la banda (se asumió que sí, como el líder) y si puede haber más de uno (se asumió uno).

## Archivos modificados
`03-requisitos.md`, `04-historias-usuario.md`, `07-criterios-aceptacion.md`, `09-casos-uso.md`, `10-diagramas-secuencia.md`, `11-diagramas-estado.md`, `12-trazabilidad.md`, `diagramas/casos-de-uso.puml`, `diagramas/dss-01-crear-convocatoria.puml`, `diagramas/dss-07-revisar-evento-masivo.puml` (nuevo), `diagramas/est-01.puml`. El modelo de dominio (`08-modelo-dominio.md` y `modelo-dominio.drawio`) lo actualiza el equipo según las observaciones de esta revisión.
