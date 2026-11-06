# Trazabilidad

## Matriz de trazabilidad

Esta matriz relaciona los requisitos de la Entrega 1 con las historias de usuario y los artefactos que desarrollamos en la Entrega 2. Se consideraron los requisitos funcionales, no funcionales, de proyecto y el requisito derivado que aparecen en [03-requisitos.md](./03-requisitos.md).

Para revisar las referencias se utilizaron las [historias de usuario](./04-historias-usuario.md), los [criterios de aceptación](./07-criterios-aceptacion.md), los [casos de uso](./09-casos-uso.md), los [diagramas de secuencia](./10-diagramas-secuencia.md), los [diagramas de estado](./11-diagramas-estado.md) y el [modelo de dominio](./08-modelo-dominio.md).

| Requisito (Entrega 1) | Historia | Caso de uso | Secuencia | Estado | Clases del dominio |
|---|---|---|---|---|---|
| RF-01 | HU-01 | CU-01 | DSS-01 | EST-01 | `EventoDeEnsayo`, `Instrumento`, `Integrante`, `Banda` |
| RF-02 | HU-01 | CU-01 | DSS-01 | EST-01, EST-02 | `EventoDeEnsayo`, `Convocatoria`, `Integrante` |
| RF-03 | HU-02 | — | — | — | `Convocatoria`, `Integrante`, `EventoDeEnsayo` |
| RF-04 | HU-02 | — | — | EST-01, EST-02 | `EventoDeEnsayo`, `Asistencia` |
| RF-05 | HU-03 | — | DSS-02 | EST-02 | `Integrante`, `Asistencia`, `Instrumento` |
| RF-06 | HU-03 | — | DSS-02 | EST-02 | `EventoDeEnsayo`, `Integrante`, `Asistencia`, `Instrumento` |
| RF-07 | HU-04 | CU-02 | DSS-02 | EST-01 | `EventoDeEnsayo`, `Asistencia`, `Instrumento` |
| RF-08 | HU-04 | CU-02 | DSS-02 | EST-01 | `EventoDeEnsayo`, `Integrante` |
| RF-09 | HU-04, HU-05 | CU-02 | DSS-02 | EST-01 | `EventoDeEnsayo`, `Alerta`, `Integrante`, `Instrumento` |
| RF-10 | HU-05 | — | — | EST-01 | `EventoDeEnsayo`, `Alerta`, `Integrante`, `Convocatoria` |
| RF-11 | HU-02 | — | — | EST-01 | `EventoDeEnsayo`, `Integrante` |
| RNF-01 | HU-01, HU-05 | CU-01 | DSS-01 | EST-01 | `Integrante`, `EventoDeEnsayo` |
| RNF-02 | HU-03 | — | — | — | `Integrante`, `Asistencia`, `Instrumento` |
| RNF-03 | HU-03 | — | DSS-02 | EST-02 | `Asistencia`, `Instrumento` |
| RNF-04 | HU-01, HU-04 | CU-01, CU-02 | DSS-01, DSS-02 | EST-01 | `Convocatoria`, `EventoDeEnsayo`, `Integrante`, `Alerta` |
| RNF-05 | HU-03, HU-04 | CU-02 | DSS-02 | EST-01, EST-02 | `EventoDeEnsayo`, `Asistencia`, `Instrumento` |
| RD-01 | HU-02, HU-04 | CU-02 | DSS-02 | EST-01 | `EventoDeEnsayo` |
| RY-01 | — | — | — | — | — |
| RY-02 | — | — | — | — | — |
| RY-03 | — | — | — | — | — |
| RY-04 | — | — | — | — | — |
| RY-05 | — | — | — | — | — |
| RY-06 | — | — | — | — | — |

## Observaciones

- Las cinco historias de usuario (HU-01 a HU-05) están incluidas en la matriz. Los casos de uso y las secuencias desarrollados en esta entrega corresponden a **HU-01** (`CU-01` y `DSS-01`) y **HU-04** (`CU-02` y `DSS-02`). Por eso algunas filas tienen «—»: esas historias no cuentan con un caso de uso o secuencia propios.
- **HU-03** no tiene un caso de uso independiente, pero el mensaje `registrarAsistencia` aparece al inicio de `DSS-02` y activa la evaluación del ensayo. **HU-05** se refleja en `EST-01` con las decisiones de esperar o reagendar, aunque todavía no tiene una secuencia propia.
- En **RF-03**, abrir la notificación no cambia por sí solo el estado del evento, por eso no se relaciona con un diagrama de estado. **RF-04** y **RF-11** sí se apoyan en los estados del evento para distinguir cuándo se puede registrar asistencia y cuándo ya no está disponible; el mensaje de indisponibilidad de RF-11 no está detallado en una secuencia.
- **RNF-02**, **RNF-03** y **RNF-04** incluyen medidas de calidad (15 segundos y 3 interacciones; menos de 1 segundo; 99,5 % de entrega). Las secuencias y los estados muestran las operaciones relacionadas cuando corresponde, pero no comprueban esos valores. Se necesitarían pruebas para verificarlos.
- Los **RY-01 a RY-06** son requisitos de proyecto: equipo, respaldos, mantenimiento, costos, responsables y capacitación. No se representan directamente mediante historias, casos de uso o diagramas del comportamiento del sistema, por lo que se dejaron con «—».
- En el modelo de dominio, **Líder de Alabanza** es un rol de la clase `Integrante`, no una clase independiente. El servicio de notificaciones es externo y tampoco se incluyó como clase. Para los estados se utiliza `EventoDeEnsayo` y, para las respuestas, `Asistencia`.
- **RD-01** proviene de **RF-04** y justifica que `EventoDeEnsayo` tenga un estado identificable. El modelo de dominio considera `Vigente`, `Confirmado`, `Cancelado` y `Terminado`; en `EST-01` se detallan las situaciones de la convocatoria mientras sigue vigente.

