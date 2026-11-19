# Análisis de rediseño y propuesta TO-BE

## Mejoras identificadas por participante

| Participante | Objetivo | Problema | Mejora deseada |
|---|---|---|---|
| Líder de Alabanza | Organizar ensayos y asegurar la presencia de los roles musicales requeridos. | La convocatoria se realiza mediante WhatsApp o de manera informal, dificultando conocer claramente quién asistirá y qué instrumentos estarán disponibles. | Crear eventos estructurados indicando fecha y roles requeridos, con seguimiento automático de las confirmaciones. |
| Líder de Alabanza | Saber si existen suficientes músicos y roles para realizar el ensayo. | Actualmente debe revisar las respuestas y determinar manualmente si se cuenta con los integrantes necesarios. | Automatizar la evaluación del quórum y de los roles requeridos para el ensayo. |
| Integrante de la banda | Conocer una convocatoria y confirmar su participación de manera simple. | Las convocatorias y respuestas se realizan mediante mensajes dispersos y pueden generar confusión. | Recibir una notificación que permita acceder directamente al evento, confirmar asistencia y ver los instrumentos asignados. |
| Líder de Alabanza | Tomar una decisión cuando no se encuentran cubiertos los roles necesarios. | Cuando faltan integrantes, la decisión de esperar, cancelar o buscar otra fecha depende de revisar manualmente las respuestas. | Recibir una alerta del sistema indicando que existen condiciones pendientes y permitir decidir entre esperar nuevas confirmaciones o reagendar. |

## Iniciativas de rediseño

### Iniciativa 1: Digitalización de la convocatoria de ensayo

- **Actividad(es) del AS-IS que afecta:** Proponer ensayo por WhatsApp o durante una reunión.
- **Heurística aplicada:** *Centralización de información*.
- **Objetivo o mejora que resuelve:** Reemplazar una convocatoria informal por un evento estructurado que contenga la fecha y los músicos convocados con los instrumentos que cubrirá cada uno.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Reduce el tiempo necesario para comunicar los datos del ensayo.
  - **Calidad:** Evita que la información importante se pierda entre conversaciones.
  - **Flexibilidad:** Permite convocar solo a los músicos necesarios y asignarles los instrumentos de cada ensayo.

### Iniciativa 2: Confirmación estructurada de asistencia

- **Actividad(es) del AS-IS que afecta:** Responder mediante mensajes indicando asistencia o inasistencia.
- **Heurística aplicada:** *Estandarización de tareas* y *enriquecimiento de información*.
- **Objetivo o mejora que resuelve:** Permitir que cada integrante confirme su asistencia directamente dentro del evento y vea los instrumentos que el líder le asignó.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Reduce la necesidad de revisar mensajes individualmente.
  - **Calidad:** Entrega información estructurada sobre la asistencia y los instrumentos asignados.
  - **Flexibilidad:** El líder puede asignar varios instrumentos a un mismo músico según el ensayo.

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

### Iniciativa 6: Perfil instrumental del músico

- **Actividad(es) del AS-IS que afecta:** No existe una actividad de registro; el instrumento de cada integrante se conoce por conversaciones informales.
- **Heurística aplicada:** *Centralización de información*.
- **Objetivo o mejora que resuelve:** Registrar el instrumento principal de cada integrante para que el líder lo use como base al crear un evento de ensayo.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Evita preguntar a cada músico con qué instrumento participará.
  - **Calidad:** Reduce errores al asignar instrumentos en el evento.
  - **Flexibilidad:** El líder puede cambiar o sumar instrumentos según el ensayo.

### Iniciativa 7: Repertorio opcional del evento

- **Actividad(es) del AS-IS que afecta:** No existe una actividad de selección; el repertorio se acuerda informalmente y no queda asociado a la convocatoria.
- **Heurística aplicada:** *Flexibilidad* y *centralización de información*.
- **Objetivo o mejora que resuelve:** Permitir que el evento incluya, de forma opcional, canciones del catálogo de la banda. El bloque de selección se muestra activado por defecto y puede desactivarse para reuniones u otras actividades sin ensayo.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Tiempo:** Evita comunicar el repertorio por mensajes separados.
  - **Calidad:** El repertorio queda registrado junto con el evento y no se pierde entre conversaciones.
  - **Flexibilidad:** Un mismo evento puede crearse con canciones, sin canciones o con el bloque de repertorio desactivado.

## Diagrama TO-BE

[Proceso TO-BE]<img width="1463" height="616" alt="Screenshot 2026-09-27 173010" src="https://github.com/user-attachments/assets/28e1f204-48b7-40a6-adfb-f367dab6b15e" />

Archivo fuente editable: [`TO-BE.bpmn`](./diagramas/TO-BE.bpmn)

La selección opcional del repertorio de canciones (HU-07) se representa dentro de la tarea de usuario «Crear evento convocando músicos y asignando sus instrumentos»; no requiere una tarea nueva en el BPMN.

### Tipos de tareas representadas

#### User Task
Tareas realizadas por una persona mediante interacción con el sistema:

- **Crear evento convocando músicos y asignando sus instrumentos** — Líder de Alabanza. Incluye, de forma opcional, la selección del repertorio de canciones (HU-07).
- **Abrir notificación para acceder al evento** — Integrante de la banda.
- **Confirmar asistencia al ensayo** — Integrante de la banda.
- **Recibir alerta de sistema y decidir acción (esperar o re-agendar)** — Líder de Alabanza.
- **Registrar el perfil instrumental del integrante** — Integrante de la banda.

#### Service Task
Tareas realizadas automáticamente por el sistema:

- **Registrar evento y notificar a los músicos convocados.**
- **Registrar asistencia y asignación de instrumentos.**
- **Bloquear agenda y notificar ensayo oficial.**

#### Compuertas de decisión

- **¿El evento sigue vigente y no ha sido cancelado?**
- **¿Se completó el quórum y los roles requeridos?**

Estas compuertas determinan si el integrante puede continuar registrando su asistencia y si el ensayo puede ser confirmado oficialmente.

## Actividades que cambian del AS-IS al TO-BE

| Actividad en el AS-IS | Actividad en el TO-BE | Qué cambia |
|---|---|---|
| Proponer ensayo por WhatsApp o durante una reunión | Crear evento convocando músicos y asignando sus instrumentos | La convocatoria deja de ser un mensaje informal y pasa a registrarse como un evento estructurado donde el líder elige a los músicos y con qué instrumentos participará cada uno. |
| Comunicar la convocatoria mediante mensajes | Registrar evento y notificar a los músicos convocados | El sistema registra el evento y notifica automáticamente a los músicos convocados. |
| Leer mensajes del grupo para conocer la convocatoria | Abrir notificación para acceder al evento | El integrante accede directamente al evento desde la notificación recibida. |
| Responder mediante mensajes confirmando asistencia o inasistencia | Confirmar asistencia al ensayo | La respuesta pasa a realizarse mediante una interfaz estructurada que muestra los instrumentos asignados por el líder. |
| Revisar manualmente las respuestas de los músicos | Registrar asistencia y asignación de instrumentos | El sistema almacena automáticamente la asistencia y los instrumentos asignados en la convocatoria. |
| Determinar manualmente si existen suficientes integrantes para realizar el ensayo | Evaluar si se completó el quórum y los roles requeridos | El sistema analiza automáticamente las confirmaciones y determina si se encuentran cubiertas las condiciones necesarias para confirmar el ensayo. |
| Confirmar manualmente que el ensayo se realizará | Bloquear agenda y notificar ensayo oficial | Al cumplirse las condiciones requeridas, el sistema confirma automáticamente el ensayo y comunica el resultado. |
| Cancelar el ensayo o volver a consultar cuando faltan integrantes | Recibir alerta de sistema y decidir acción (esperar o re-agendar) | El sistema informa al líder de la situación y este decide si mantiene el evento esperando nuevas respuestas o lo reagenda. |
| No existía | Registrar el perfil instrumental del integrante | El sistema conserva el instrumento principal de cada músico para usarlo como base al convocar. |
| No existía | Seleccionar el repertorio opcional del evento (dentro de «Crear evento») | El repertorio deja de acordarse por mensajes separados y queda registrado en el evento. El bloque se muestra activado por defecto y puede desactivarse para reuniones u otras actividades. |

## Relación con las historias de usuario

| Actividad TO-BE | Historia de usuario asociada |
|---|---|
| Crear evento convocando músicos y asignando sus instrumentos | HU-01 |
| Abrir notificación para acceder al evento | HU-02 |
| Confirmar asistencia al ensayo | HU-03 |
| Evaluar si se completó el quórum y los roles requeridos | HU-04 |
| Recibir alerta de sistema y decidir acción (esperar o re-agendar) | HU-05 |
| Registrar el perfil instrumental del integrante | HU-06 |
| Seleccionar el repertorio opcional del evento (dentro de «Crear evento convocando músicos y asignando sus instrumentos») | HU-07 |

De esta forma, las principales actividades nuevas o modificadas del proceso TO-BE quedan asociadas explícitamente a las historias de usuario correspondientes.
