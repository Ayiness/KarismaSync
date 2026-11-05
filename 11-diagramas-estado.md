# Diagramas de estado

Para esta parte se muestran los cambios de estado de dos elementos de KarismaSync: el evento de ensayo y la asistencia de cada integrante. Esto permite ver qué pasa desde que se crea una convocatoria hasta que se confirma, termina o se cancela.

## EST-01 — Ciclo de vida del evento de ensayo

- **Clase del dominio:** Evento de ensayo ([modelo de dominio](./08-modelo-dominio.md)).
- **Historias relacionadas:** [HU-01](./04-historias-usuario.md), HU-02, HU-04 y HU-05.
- **Diagramas de secuencia relacionados:** [DSS-01 y DSS-02](./10-diagramas-secuencia.md).

![EST-01 — Evento de ensayo](./diagramas/est-01.png)

**Archivo editable:** [est-01.drawio](./diagramas/est-01.drawio).

El evento comienza con una **Convocatoria abierta**. A medida que los integrantes responden, el sistema revisa si se cumple el quórum y si están cubiertos los instrumentos o roles necesarios. Si todavía falta algo, el evento pasa a **Condiciones pendientes** y el líder puede decidir si espera o reagenda. Cuando se cumplen las condiciones, el ensayo queda **Confirmado**. Después puede pasar a **Terminado** o **Cancelado**.

### Tabla de transiciones — EST-01

| Estado origen | Evento | Guarda | Acción | Estado destino |
|---|---|---|---|---|
| Inicial | `crearEvento` | Líder autorizado | Registrar el ensayo y enviar la convocatoria | Convocatoria abierta |
| Convocatoria abierta | `registrarAsistencia` | Falta quórum o algún rol | Evaluar respuestas y avisar al líder | Condiciones pendientes |
| Convocatoria abierta | `registrarAsistencia` | Quórum y roles completos | Confirmar el ensayo, bloquear agenda y notificar | Confirmado |
| Condiciones pendientes | `registrarAsistencia` | Quórum y roles completos | Confirmar el ensayo, bloquear agenda y notificar | Confirmado |
| Condiciones pendientes | `decidirEsperar` | Decisión del líder | Mantener abierta la convocatoria | En espera |
| En espera | `reagendarEvento` | Decisión del líder | Cambiar la fecha y avisar a los integrantes | Convocatoria abierta |
| En espera | `registrarAsistencia` | Quórum y roles completos | Confirmar el ensayo, bloquear agenda y notificar | Confirmado |
| Confirmado | `ensayoFinalizado` | — | Cerrar el evento | Terminado |
| Confirmado | `cancelacionRegistrada` | — | Informar la cancelación | Cancelado |
| Terminado | Fin del ciclo | — | — | Final |
| Cancelado | Fin del ciclo | — | — | Final |

**Nota:** la Entrega 1 menciona eventos cancelados, pero no explica cómo se realiza la cancelación. Por eso se muestra como `cancelacionRegistrada`, sin agregar un procedimiento que el equipo todavía no ha definido.

## EST-02 — Ciclo de vida de la asistencia

- **Clase del dominio:** Asistencia ([modelo de dominio](./08-modelo-dominio.md)).
- **Historias relacionadas:** [HU-02 y HU-03](./04-historias-usuario.md).
- **Diagrama de secuencia relacionado:** [DSS-02](./10-diagramas-secuencia.md), porque el registro de asistencia da inicio a la evaluación del ensayo.

![EST-02 — Asistencia](./diagramas/est-02.png)

**Archivo editable:** [est-02.drawio](./diagramas/est-02.drawio).

Este diagrama muestra cómo queda registrada la respuesta de un integrante. Al recibir la convocatoria, su asistencia está **Pendiente**. Si confirma que irá y señala sus instrumentos, pasa a **Confirmada**. También puede indicar que **No asiste**. Si el evento se cancela o termina antes de que responda, queda **Sin respuesta**.

### Tabla de transiciones — EST-02

| Estado origen | Evento | Guarda | Acción | Estado destino |
|---|---|---|---|---|
| Inicial | Convocatoria emitida | — | Dejar disponible la respuesta | Pendiente |
| Pendiente | `registrarAsistencia` | Evento vigente y confirma con instrumentos | Guardar la asistencia y los instrumentos | Confirmada |
| Pendiente | `registrarAsistencia` | Evento vigente y señala que no asistirá | Registrar que no asistirá | No asiste |
| Pendiente | `registrarAsistencia` | Confirma, pero no indica instrumentos | No guardar la respuesta incompleta | Pendiente |
| Pendiente | Evento cancelado o terminado | El integrante no ha respondido | Cerrar la convocatoria para ese integrante | Sin respuesta |
| Confirmada | Fin de la respuesta | — | — | Final |
| No asiste | Fin de la respuesta | — | — | Final |
| Sin respuesta | Fin de la respuesta | — | — | Final |

La asistencia **Confirmada** de un integrante no significa que todo el ensayo esté confirmado. Para eso, KarismaSync también revisa el quórum y los roles necesarios.
