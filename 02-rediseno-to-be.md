# Análisis de rediseño y propuesta TO-BE

## Mejoras identificadas por participante

| Participante | Objetivo | Problema | Mejora deseada |
|---|---|---|---|
| Líder de Alabanza | Organizar ensayos y asegurar la presencia de los roles musicales requeridos. | La convocatoria se realiza mediante WhatsApp o de manera informal, dificultando conocer claramente quién asistirá y qué instrumentos estarán disponibles. | Crear eventos estructurados indicando fecha y roles requeridos, con seguimiento automático de las confirmaciones. |
| Líder de Alabanza | Saber si existen suficientes músicos y roles para realizar el ensayo. | Actualmente debe revisar las respuestas y determinar manualmente si se cuenta con los integrantes necesarios. | Automatizar la evaluación del quórum y de los roles requeridos para el ensayo. |
| Integrante de la banda | Conocer una convocatoria y confirmar su participación de manera simple. | Las convocatorias y respuestas se realizan mediante mensajes dispersos y pueden generar confusión. | Recibir una notificación que permita acceder directamente al evento, confirmar asistencia e indicar uno o múltiples instrumentos. |
| Líder de Alabanza | Tomar una decisión cuando no se encuentran cubiertos los roles necesarios. | Cuando faltan integrantes, la decisión de esperar, cancelar o buscar otra fecha depende de revisar manualmente las respuestas. | Recibir una alerta del sistema indicando que existen condiciones pendientes y permitir decidir entre esperar nuevas confirmaciones o reagendar. |

## Iniciativas de rediseño

### Iniciativa 1: Digitalización de la convocatoria de ensayo

- **Actividad(es) del AS-IS que afecta:** Proponer ensayo por WhatsApp o durante una reunión.
- **Heurística aplicada:** *Centralización de información*.
- **Objetivo o mejora que resuelve:** Reemplazar una convocatoria informal por un evento estructurado que contenga la fecha y los roles musicales requeridos.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Reduce el tiempo necesario para comunicar los datos del ensayo.
  - **Calidad:** Evita que la información importante se pierda entre conversaciones.
  - **Flexibilidad:** Permite definir los roles requeridos según las necesidades de cada ensayo.

### Iniciativa 2: Confirmación estructurada de asistencia e instrumentos

- **Actividad(es) del AS-IS que afecta:** Responder mediante mensajes indicando asistencia o inasistencia.
- **Heurística aplicada:** *Estandarización de tareas* y *enriquecimiento de información*.
- **Objetivo o mejora que resuelve:** Permitir que cada integrante confirme su asistencia directamente dentro del evento e indique uno o múltiples instrumentos con los que participará.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Reduce la necesidad de revisar mensajes individualmente.
  - **Calidad:** Entrega información estructurada sobre la asistencia y los instrumentos disponibles.
  - **Flexibilidad:** Permite representar músicos que desempeñan más de un rol instrumental.

### Iniciativa 3: Automatización del registro y evaluación del quórum

- **Actividad(es) del AS-IS que afecta:** Revisar manualmente quién confirmó asistencia y decidir si existen suficientes músicos para realizar el ensayo.
- **Heurística aplicada:** *Automatización de tareas* y *reducción de variabilidad*.
- **Objetivo o mejora que resuelve:** Registrar automáticamente al músico y sus instrumentos en el evento y evaluar si se ha completado el quórum y los roles requeridos.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Reduce el trabajo manual necesario para revisar las confirmaciones.
  - **Calidad:** Disminuye errores al determinar qué roles musicales se encuentran cubiertos.
  - **Flexibilidad:** La evaluación se adapta a los roles definidos al crear cada evento.

### Iniciativa 4: Gestión de excepciones y reagendamiento

- **Actividad(es) del AS-IS que afecta:** Cancelar el ensayo o volver a consultar informalmente cuando no existen suficientes integrantes.
- **Heurística aplicada:** *Notificación proactiva por excepción*.
- **Objetivo o mejora que resuelve:** Informar al líder cuando no se complete el quórum o falten roles requeridos, permitiéndole decidir si espera nuevas confirmaciones o reagenda el ensayo.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** El líder conoce inmediatamente que existen condiciones pendientes.
  - **Calidad:** La decisión se toma utilizando información registrada en el sistema.
  - **Flexibilidad:** El líder conserva la decisión final sobre esperar o reagendar.

### Iniciativa 5: Confirmación automática del ensayo

- **Actividad(es) del AS-IS que afecta:** Confirmar manualmente a los integrantes que el ensayo se realizará.
- **Heurística aplicada:** *Automatización de tareas*.
- **Objetivo o mejora que resuelve:** Una vez cumplido el quórum y los roles requeridos, el sistema confirma automáticamente el ensayo y notifica a los integrantes.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Reduce la comunicación manual posterior a la confirmación.
  - **Calidad:** Entrega una confirmación oficial y consistente a todos los integrantes.

## Diagrama TO-BE

[Proceso TO-BE]<img width="1463" height="616" alt="Screenshot 2026-09-27 173010" src="https://github.com/user-attachments/assets/28e1f204-48b7-40a6-adfb-f367dab6b15e" />

Archivo fuente editable: [`TO-BE.bpmn`](./diagramas/TO-BE.bpmn)

### Tipos de tareas representadas

#### User Task
Tareas realizadas por una persona mediante interacción con el sistema:

- **Crear evento indicando fecha y roles requeridos** — Líder de Alabanza.
- **Abrir notificación para acceder al evento** — Integrante de la banda.
- **Confirmar asistencia y seleccionar uno o múltiples instrumentos** — Integrante de la banda.
- **Recibir alerta de sistema y decidir acción (esperar o re-agendar)** — Líder de Alabanza.

#### Service Task
Tareas realizadas automáticamente por el sistema:

- **Registrar evento y notificar a la banda.**
- **Registrar músico e instrumentos en el evento.**
- **Bloquear agenda y notificar ensayo oficial.**

#### Compuertas de decisión

- **¿El evento sigue vigente y no ha sido cancelado?**
- **¿Se completó el quórum y los roles requeridos?**

Estas compuertas determinan si el integrante puede continuar registrando su asistencia y si el ensayo puede ser confirmado oficialmente.

## Actividades que cambian del AS-IS al TO-BE

| Actividad en el AS-IS | Actividad en el TO-BE | Qué cambia |
|---|---|---|
| Proponer ensayo por WhatsApp o durante una reunión | Crear evento indicando fecha y roles requeridos | La convocatoria deja de ser un mensaje informal y pasa a registrarse como un evento estructurado dentro del sistema. |
| Comunicar la convocatoria mediante mensajes | Registrar evento y notificar a la banda | El sistema registra el evento y notifica automáticamente a los integrantes. |
| Leer mensajes del grupo para conocer la convocatoria | Abrir notificación para acceder al evento | El integrante accede directamente al evento desde la notificación recibida. |
| Responder mediante mensajes confirmando asistencia o inasistencia | Confirmar asistencia y seleccionar uno o múltiples instrumentos | La respuesta pasa a realizarse mediante una interfaz estructurada que además permite indicar los instrumentos con los que participará el integrante. |
| Revisar manualmente las respuestas de los músicos | Registrar músico e instrumentos en el evento | El sistema almacena automáticamente la asistencia y los instrumentos declarados por cada integrante. |
| Determinar manualmente si existen suficientes integrantes para realizar el ensayo | Evaluar si se completó el quórum y los roles requeridos | El sistema analiza automáticamente las confirmaciones y determina si se encuentran cubiertas las condiciones necesarias para confirmar el ensayo. |
| Confirmar manualmente que el ensayo se realizará | Bloquear agenda y notificar ensayo oficial | Al cumplirse las condiciones requeridas, el sistema confirma automáticamente el ensayo y comunica el resultado. |
| Cancelar el ensayo o volver a consultar cuando faltan integrantes | Recibir alerta de sistema y decidir acción (esperar o re-agendar) | El sistema informa al líder de la situación y este decide si mantiene el evento esperando nuevas respuestas o lo reagenda. |

## Relación con las historias de usuario

| Actividad TO-BE | Historia de usuario asociada |
|---|---|
| Crear evento indicando fecha y roles requeridos | HU-01 |
| Abrir notificación para acceder al evento | HU-02 |
| Confirmar asistencia y seleccionar uno o múltiples instrumentos | HU-03 |
| Evaluar si se completó el quórum y los roles requeridos | HU-04 |
| Recibir alerta de sistema y decidir acción (esperar o re-agendar) | HU-05 |

De esta forma, las principales actividades nuevas o modificadas del proceso TO-BE quedan asociadas explícitamente a las historias de usuario correspondientes.
