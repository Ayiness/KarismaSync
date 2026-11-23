# Trazabilidad

## Matriz de trazabilidad

Esta matriz relaciona los requisitos de la Entrega 1 con las historias de usuario y los artefactos que desarrollamos en la Entrega 2. Se consideraron los requisitos funcionales, no funcionales, de proyecto y el requisito derivado que aparecen en [03-requisitos.md](./03-requisitos.md).

Para revisar las referencias se utilizaron las [historias de usuario](./04-historias-usuario.md), los [criterios de aceptación](./07-criterios-aceptacion.md), los [casos de uso](./09-casos-uso.md), los [diagramas de secuencia](./10-diagramas-secuencia.md), los [diagramas de estado](./11-diagramas-estado.md) y el [modelo de dominio](./08-modelo-dominio.md).

| Requisito (Entrega 1) | Historia | Caso de uso | Secuencia | Estado | Clases del dominio |
|---|---|---|---|---|---|
| RF-01 | HU-01 | CU-01 | DSS-01 | EST-01 | `EventoDeEnsayo`, `Instrumento`, `Integrante`, `Banda` |
| RF-02 | HU-01 | CU-01 | DSS-01 | EST-01, EST-02 | `EventoDeEnsayo`, `Convocatoria`, `Integrante` |
| RF-03 | HU-02 | — | — | — | `Convocatoria`, `Integrante`, `EventoDeEnsayo` |
| RF-04 | HU-02, HU-03 | CU-05 | DSS-05 | EST-01, EST-02 | `EventoDeEnsayo`, `Asistencia` |
| RF-05 | HU-03 | CU-05 | DSS-05, DSS-02 | EST-02 | `Integrante`, `Convocatoria`, `Asistencia`, `Instrumento` |
| RF-06 | HU-03 | CU-05 | DSS-05, DSS-02 | EST-02 | `EventoDeEnsayo`, `Convocatoria`, `Asistencia`, `Instrumento` |
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
| RF-12 | HU-06 | CU-03 | DSS-03 | — | `Integrante`, `Instrumento` |
| RF-13 | HU-07 | CU-04 | DSS-04 | — | `EventoDeEnsayo`, `Cancion` |
| RF-14 | HU-03 | CU-05, CU-06 | DSS-05, DSS-06 | EST-02 | `Convocatoria`, `Asistencia`, `Integrante`, `Instrumento` |
| RD-01 | HU-02, HU-04 | CU-02 | DSS-02 | EST-01 | `EventoDeEnsayo` |
| RY-01 | — | — | — | — | — |
| RY-02 | — | — | — | — | — |
| RY-03 | — | — | — | — | — |
| RY-04 | — | — | — | — | — |
| RY-05 | — | — | — | — | — |
| RY-06 | — | — | — | — | — |

## Historias implementadas: código y pruebas

Cada historia implementada se enlaza con su cambio de OpenSpec, el código que la realiza y la prueba automática de cada escenario Gherkin de [07-criterios-aceptacion.md](./07-criterios-aceptacion.md).

| Historia | Cambio OpenSpec | Código (rutas / funciones / tablas) | Escenario Gherkin → prueba automática |
|----------|-----------------|-------------------------------------|----------------------------------------|
| HU-01 | `hu-01-crear-evento-ensayo`, `hu-01-quorum-obligatorio` | `GET /eventos/nuevo`, `POST /eventos`, `GET /eventos/{id}` en [`app/rutas/eventos.py`](./app/rutas/eventos.py); `crear_evento` en [`app/servicios/crear_evento.py`](./app/servicios/crear_evento.py); `EventoDeEnsayo` y `transicionar` en [`app/dominio/evento_ensayo.py`](./app/dominio/evento_ensayo.py); tablas `eventos_ensayo`, `convocatorias`, `convocatorias_instrumentos` | La lista de convocados muestra a todos los músicos con su instrumento principal → `test_formulario_muestra_los_musicos_con_su_instrumento_principal` ([test_pantallas.py](./tests/test_pantallas.py))<br>El líder crea un evento convocando a toda la banda → `test_hu01_el_lider_crea_evento_y_convoca_a_toda_la_banda`<br>El líder convoca solo a los músicos que necesita → `test_hu01_el_lider_convoca_solo_a_los_musicos_que_necesita`<br>El líder cambia o suma instrumentos a un músico convocado → `test_hu01_el_lider_cambia_o_suma_instrumentos_a_un_convocado`<br>Un integrante sin rol de líder intenta crear un evento → `test_hu01_integrante_sin_rol_de_lider_no_crea_evento`<br>El líder intenta crear un evento sin músicos convocados → `test_hu01_lider_sin_musicos_convocados_no_crea_evento`<br>El líder intenta crear un evento con un músico sin instrumentos → `test_hu01_lider_con_musico_convocado_sin_instrumentos_no_crea_evento`<br>El líder intenta crear un evento de ensayo sin quórum → `test_hu01_lider_sin_quorum_no_crea_evento`<br>El líder intenta crear un evento con un quórum mayor que los músicos convocados → `test_hu01_lider_con_quorum_mayor_que_convocados_no_crea_evento`<br>(todas en [test_hu01_crear_evento.py](./tests/test_hu01_crear_evento.py) salvo la primera) |
| HU-06 | `hu-06-perfil-instrumental` | `GET /perfil`, `POST /perfil` (`perfil`, `guardar_perfil`) en [`app/rutas/eventos.py`](./app/rutas/eventos.py); tabla `integrantes_instrumentos` | El integrante registra su instrumento principal → `test_hu06_el_integrante_registra_su_instrumento_principal`<br>El integrante cambia su instrumento principal → `test_hu06_el_integrante_cambia_su_instrumento_principal`<br>El integrante intenta registrar su perfil sin instrumento principal → `test_hu06_el_integrante_intenta_registrar_su_perfil_sin_instrumento_principal`<br>(en [test_hu06_perfil_instrumental.py](./tests/test_hu06_perfil_instrumental.py)) |
| HU-07 | `hu-07-repertorio-opcional` | `GET /eventos/nuevo`, `POST /eventos` (bloque `incluir_repertorio`), `GET /eventos/{id}`; `crear_evento` (`canciones_ids`); tablas `canciones`, `eventos_canciones` | El formulario ofrece el repertorio activado por defecto → `test_hu07_formulario_ofrece_repertorio_activo_y_catalogo_de_20`<br>El líder crea un evento con canciones seleccionadas → `test_hu07_lider_crea_evento_con_canciones_seleccionadas`<br>El líder crea un evento sin repertorio porque es una reunión → `test_hu07_lider_crea_evento_sin_repertorio_al_desactivar`<br>El líder deja el repertorio activado pero no selecciona canciones → `test_hu07_lider_deja_repertorio_activo_sin_canciones`<br>Las canciones no seleccionadas no se asocian al evento → `test_hu07_canciones_no_seleccionadas_no_se_asocian`<br>(en [test_hu07_repertorio.py](./tests/test_hu07_repertorio.py)) |
| HU-0X | _(cuarta historia, pendiente)_ | — | — |

Pruebas de apoyo (no son escenarios Gherkin): EST-01 `Inicial → Vigente` y transición no permitida en [test_evento_ensayo.py](./tests/test_evento_ensayo.py); validaciones del servicio en [test_crear_evento.py](./tests/test_crear_evento.py); integración simulada de notificaciones en [test_notificaciones.py](./tests/test_notificaciones.py).

## Observaciones

- Las siete historias de usuario (HU-01 a HU-07) están incluidas en la matriz. Los casos de uso y las secuencias desarrollados en esta entrega corresponden a **HU-01** (`CU-01` y `DSS-01`), **HU-04** (`CU-02` y `DSS-02`), **HU-06** (`CU-03` y `DSS-03`), **HU-07** (`CU-04` y `DSS-04`) y **HU-03** (`CU-05`/`DSS-05` y `CU-06`/`DSS-06`). Por eso algunas filas tienen «—»: esas historias no cuentan con un caso de uso o secuencia propios.
- **HU-03** se representa con `CU-05` (responder la convocatoria) y `CU-06` (revisar las respuestas). El mensaje `registrarAsistencia(evento, asiste, motivo)` de `DSS-05` es el mismo que inicia `DSS-02`, donde activa la evaluación del ensayo (HU-04). **HU-05** se refleja en `EST-01` con las decisiones de esperar o reagendar, aunque todavía no tiene una secuencia propia.
- En **RF-03**, abrir la notificación no cambia por sí solo el estado del evento, por eso no se relaciona con un diagrama de estado. **RF-04** y **RF-11** sí se apoyan en los estados del evento para distinguir cuándo se puede registrar asistencia y cuándo ya no está disponible; el mensaje de indisponibilidad de RF-11 no está detallado en una secuencia.
- **RNF-02**, **RNF-03** y **RNF-04** incluyen medidas de calidad (15 segundos y 3 interacciones; menos de 1 segundo; 99,5 % de entrega). Las secuencias y los estados muestran las operaciones relacionadas cuando corresponde, pero no comprueban esos valores. Se necesitarían pruebas para verificarlos.
- Los **RY-01 a RY-06** son requisitos de proyecto: equipo, respaldos, mantenimiento, costos, responsables y capacitación. No se representan directamente mediante historias, casos de uso o diagramas del comportamiento del sistema, por lo que se dejaron con «—».
- En el modelo de dominio, **Líder de Alabanza** es un rol de la clase `Integrante`, no una clase independiente. El servicio de notificaciones es externo y tampoco se incluyó como clase. Para los estados se utiliza `EventoDeEnsayo` y, para las respuestas, `Asistencia`.
- **RD-01** proviene de **RF-04** y justifica que `EventoDeEnsayo` tenga un estado identificable. El modelo de dominio considera `Vigente`, `Confirmado`, `Cancelado` y `Terminado`; en `EST-01` se detallan las situaciones de la convocatoria mientras sigue vigente.
- **HU-06** y **HU-07** no modifican los diagramas de estado: el instrumento principal es un dato del integrante y el repertorio es un dato opcional del evento, por lo que no cambian el ciclo de vida (véase la nota en `11-diagramas-estado.md`).
