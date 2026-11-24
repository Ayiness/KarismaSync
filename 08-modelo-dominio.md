# Modelo de dominio

## Diagrama
![Modelo de dominio](./diagramas/modelo-dominio.png)

Archivo fuente: [`./diagramas/modelo-dominio.drawio`](./diagramas/modelo-dominio.drawio)

## Descripción de las clases
| Clase | Qué representa en el negocio | Atributos |
|-------|------------------------------|-----------|
| Banda | Agrupación musical de la iglesia que organiza sus ensayos. | nombre |
| Integrante | Músico que forma parte de la banda; algunos cumplen además el rol de Líder de Alabanza. | nombre |
| EventoDeEnsayo | Ensayo propuesto para una fecha, con el quórum y los roles requeridos que lo hacen viable. | fecha, quorum, estado |
| Convocatoria | Aviso del evento de ensayo que reciben los integrantes al crearse o al reagendarse el ensayo. | fechaEnsayo, fechaEnvio |
| Asistencia | Respuesta de un músico convocado a su convocatoria: si asistirá o no y, si no asistirá, por qué. Nace Pendiente al emitirse la convocatoria. | estado, motivo, fechaRespuesta |
| Instrumento | Instrumento o rol musical (batería, bajo, guitarra eléctrica, guitarra acústica, teclado, voz) que se requiere en un ensayo, que un integrante registra como principal o que se asigna a un convocado. | nombre, esMusicoBase |
| Cancion | Canción del catálogo de la banda que puede formar parte del repertorio opcional de un evento. | titulo, autor |
| Alerta | Aviso al Líder de Alabanza de que el ensayo tiene condiciones pendientes: falta quórum o roles requeridos. | fechaEmision, integrantesFaltantes |

El atributo `estado` de EventoDeEnsayo toma los valores de la enumeración EstadoEvento: Vigente, Confirmado, Cancelado y Terminado (requisito derivado RD-01 y HU-04). El atributo `estado` de Asistencia toma los valores de la enumeración EstadoAsistencia: Pendiente, Confirmada, No asiste y Sin respuesta (EST-02 y HU-03); `motivo` es obligatorio solo cuando el estado es No asiste (máximo 200 caracteres). El atributo `esMusicoBase` identifica los músicos base acordados en la [elicitación](./05-elicitacion.md): teclado, bajo, guitarra eléctrica, guitarra acústica y batería; la guitarra se desdobla en sus dos variantes.

## Asociaciones
| Asociación | Clases | Multiplicidades | Justificación |
|------------|--------|-----------------|----------------|
| integra | Integrante – Banda | 1..* a 1 | Cada integrante pertenece a la banda, y una banda tiene al menos un integrante (HU-01: el líder convoca a los integrantes de su banda que necesita). |
| lidera | Integrante (líder) – Banda | 1..* a 0..1 | Solo el Líder de Alabanza puede crear y reagendar eventos (RNF-01). La banda tiene al menos un líder; la elicitación identificó dos responsables: el encargado y el director musical. Un integrante lidera a lo más una banda. |
| toca | Integrante – Instrumento (instrumentoPrincipal) | 1 a 0..1 | Cada integrante registra como máximo un instrumento principal (HU-06); un instrumento puede ser principal de muchos integrantes. Un integrante sin perfil registrado aún no tiene principal. |
| organiza | Banda – EventoDeEnsayo | 1 a 0..* | Cada evento de ensayo pertenece a una banda; una banda puede no tener ensayos o tener muchos (RF-01). |
| requiere | EventoDeEnsayo – Instrumento (rolesRequeridos) | 0..* a 1..* | Un evento tiene al menos un rol requerido porque exige al menos un músico convocado con al menos un instrumento (HU-01, CA8); un mismo instrumento puede requerirse en muchos eventos. Se deriva de la unión de los instrumentos asignados en las convocatorias. |
| incluye | EventoDeEnsayo – Cancion (repertorio) | 0..* a 0..* | Un evento puede incluir cero o más canciones del catálogo y una canción puede estar en muchos eventos. La ausencia de canciones representa un evento sin repertorio, como una reunión de coordinación (HU-07). |
| emite | EventoDeEnsayo – Convocatoria | 1 a 1..* | Al crear el evento se emite su convocatoria (RF-02), y al reagendarlo se emite una nueva con la fecha actualizada (HU-05). |
| es recibida por | Convocatoria – Integrante | 0..* a 1..* | Solo los integrantes convocados reciben la convocatoria (HU-01); un integrante recibe convocatorias de distintos eventos. |
| asigna | Convocatoria – Instrumento (instrumentosDelConvocado) | 1 a 1..* | El líder convoca a cada músico con uno o más instrumentos, que pueden o no incluir su principal (HU-01); un instrumento puede asignarse en muchas convocatorias. |
| tiene | Convocatoria – Asistencia | 1 a 1 | Cada convocatoria tiene exactamente una asistencia, que nace Pendiente al emitirse (EST-02) y guarda la respuesta del convocado y su motivo (HU-03, RF-06). Reemplaza a la asociación `registra` (EventoDeEnsayo – Asistencia): las asistencias de un evento son las de sus convocatorias. |
| responde | Integrante – Asistencia | 1 a 0..* | Cada asistencia es la respuesta de un integrante; un integrante responde en distintos eventos, a lo más una vez por evento. |
| genera | EventoDeEnsayo – Alerta | 1 a 0..* | La evaluación del quórum y los roles genera una alerta cuando quedan condiciones pendientes (RF-09); si el ensayo se confirma, no se genera ninguna. |
| se envía a | Alerta – Integrante (líder) | 0..* a 1..* | La alerta se dirige al Líder de Alabanza para que decida esperar o reagendar (HU-05). |
| señala | Alerta – Instrumento (rolesFaltantes) | 0..* a 0..* | La alerta indica qué rol falta (HU-04: «falta el rol batería»); si solo falta quórum, no señala ningún instrumento y usa `integrantesFaltantes`. |

## Decisiones de modelado
- **Líder de Alabanza se modeló como rol y no como clase.** Un líder es un integrante más de la banda que además coordina los ensayos; crear una clase aparte duplicaría a la persona. Se representa como el extremo «líder» de las asociaciones `lidera` y `se envía a`. El encargado y el director musical de la elicitación son dos integrantes con ese rol.
- **Instrumento cumple dos roles en el dominio:** `rolesRequeridos` en el evento y `rolesFaltantes` en la alerta. Se usa una sola clase porque el negocio habla del mismo catálogo («roles requeridos batería, bajo y voz», «con el instrumento voz»).
- **El instrumento principal es una asociación, no un atributo duplicado.** Se modela con `toca` (Integrante – Instrumento) para reutilizar el catálogo y evitar guardar el nombre del instrumento dos veces (HU-06). La multiplicidad 1–0..1 expresa que solo se registra el principal y que un perfil puede estar aún incompleto.
- **El repertorio se modela como asociación y no como un booleano en el evento.** `incluye` (EventoDeEnsayo – Cancion) con 0..* en ambos extremos expresa que las canciones son opcionales. No se agrega un atributo «incluyeRepertorio» porque el evento sin canciones ya representa el caso de una reunión; el bloque activado por defecto es una decisión de interfaz (HU-07) y no un estado del dominio.
- **`rolesRequeridos` se deriva de las convocatorias.** El líder asigna instrumentos a cada músico convocado en `asigna`; el conjunto de roles requeridos del evento es la unión de esos instrumentos. Así HU-04 sigue comparando la cobertura sin un catálogo paralelo en el evento.
- **Se usó composición** entre EventoDeEnsayo y sus Convocatorias y Alertas, y entre cada Convocatoria y su Asistencia, porque ninguna tiene sentido fuera del todo al que pertenece: si el evento no existiera, tampoco existirían su convocatoria, la respuesta a ella ni sus alertas.
- **La respuesta se modela con un estado y no con un booleano.** `asiste` no distinguía entre «todavía no responde» y «no asistirá»; EstadoAsistencia sí, y permite que la respuesta cambie mientras el evento esté vigente (HU-03, CA7). Los instrumentos de la asistencia son los asignados en la convocatoria (`asigna`): el integrante no los declara.
- **No se usó agregación** entre Banda e Integrante: es una asociación simple (`integra`), porque el integrante es una persona que existe por sí misma y la relación no expresa una relación todo-parte relevante para el negocio.
- **No se usó herencia:** no hay subtipos del negocio con atributos propios; Líder de Alabanza es un rol, no un subtipo.
- **El servicio de notificaciones no es una clase del dominio:** es un sistema externo y aparece como actor en los [casos de uso](./09-casos-uso.md) y como participante en los [diagramas de secuencia](./10-diagramas-secuencia.md).
- **«En espera» no es un estado propio del evento:** según HU-05, cuando el líder decide esperar, el ensayo «sigue vigente y sin confirmar», por lo que se representa como EventoDeEnsayo en estado Vigente con una Alerta generada. El ciclo de vida detallado de EstadoEvento se describe en los [diagramas de estado](./11-diagramas-estado.md).
- **La agenda de la banda no se modeló como clase:** bloquear la agenda (RF-08) corresponde a que el EventoDeEnsayo pase al estado Confirmado. La regla exacta de qué agenda se bloquea sigue pendiente de validación, como se indica en los casos de uso.

Hecho clases 24/11
<img width="4080" height="1888" alt="modelo de dominio" src="https://github.com/user-attachments/assets/fc63b2fc-fb0f-4c09-a29b-e949f1beb7d4" />

