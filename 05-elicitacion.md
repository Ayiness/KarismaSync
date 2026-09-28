# Elicitación de requisitos

## Técnica 1: Entrevista semiestructurada

- **Participante(s):** Encargado de la agrupación musical / cliente.
- **Fecha y modalidad:** 27-09-2026, presencial.
- **Tipo de técnica:** Entrevista semiestructurada con preguntas abiertas, preguntas de profundización, planteamiento de escenarios y validación de respuestas.
- **Evidencia:** Grabación de audio/video de la entrevista realizada con el cliente.

### Desarrollo de la técnica

Se preparó previamente un conjunto de preguntas relacionadas con la forma en que actualmente se coordinan los ensayos, los integrantes necesarios para realizarlos, las condiciones bajo las cuales se confirma o cancela un ensayo y las responsabilidades de las personas encargadas.

La entrevista fue semiestructurada, ya que a partir de las respuestas entregadas por el cliente se realizaron preguntas adicionales de profundización. También se plantearon escenarios hipotéticos, por ejemplo, qué ocurriría si faltara uno o más músicos base, con el objetivo de comprender las reglas reales utilizadas por la agrupación.

Durante la entrevista también se reformularon algunas respuestas del cliente para confirmar que la interpretación del equipo fuese correcta.

### Hallazgos principales

- Los ensayos funcionan principalmente como una instancia de **ensamble**, debido a que los integrantes deberían llegar con las canciones previamente practicadas de manera individual.

- Los principales **músicos base** considerados necesarios para un ensayo son:
  - Teclado.
  - Bajo.
  - Guitarra.
  - Batería.

- Las voces pueden participar en el ensayo, pero para el cliente tienen una prioridad menor que los músicos base, debido a que pueden realizar parte de su preparación individualmente y apoyarse mediante multitrack.

- Para trabajar canciones nuevas, la situación ideal es contar con todos los músicos base.

- La ausencia de un músico base todavía podría permitir la realización del ensayo, aunque el sistema debería advertir de esta situación a las personas responsables.

- Si faltan dos de los cuatro músicos base, la realización del ensayo se vuelve considerablemente más difícil y puede requerir su cancelación o reagendamiento.

- El cliente considera útil que el sistema pueda entregar una **alerta** cuando se detecte que falta un integrante o rol considerado importante.

- La agrupación organiza sus ensayos con anticipación. El cliente señaló que normalmente existe aproximadamente **un mes para organizar los ensayos**.

- Los ensayos tienen un día establecido habitualmente, correspondiente a los **martes**, práctica que la agrupación ha mantenido durante aproximadamente tres años.

- Debido a esta planificación anticipada, las cancelaciones deberían producirse principalmente por situaciones excepcionales o de fuerza mayor.

- Se identificó como posibilidad realizar una consulta o seguimiento aproximadamente **15 días antes del ensayo**, con el fin de conocer el estado o disponibilidad de los participantes.

- La agrupación posee **dos personas con responsabilidades administrativas**:
  - El encargado.
  - El director musical.

- El **encargado** tiene una función principalmente organizativa y de gestión, incluyendo la planificación o agendamiento de los ensayos.

- El **director musical** se concentra principalmente en los aspectos técnicos y musicales y en el estado de preparación de los integrantes.

- Ambos responsables deberían tener participación en las decisiones relacionadas con los ensayos.

- El cliente considera necesario mantener algún tipo de **registro o bitácora posterior al ensayo**.

- Tanto el encargado como el director musical deberían poder gestionar o modificar esta información.

### Conclusiones de la entrevista

La entrevista permitió determinar que la realización de un ensayo no depende únicamente de alcanzar un porcentaje general de asistencia. La presencia de determinados roles instrumentales es un factor importante para decidir si el ensayo puede realizarse.

Por esta razón, el sistema debería registrar tanto la disponibilidad de los integrantes como los instrumentos o roles que pueden desempeñar y utilizar esta información para apoyar la decisión de confirmar, mantener en espera o reagendar un ensayo.

---

## Técnica 2: Revisión documental

- **Participante(s):** Equipo de desarrollo.
- **Fuente revisada:** Conversaciones y capturas utilizadas por la agrupación para coordinar sus actividades y ensayos.
- **Modalidad:** Revisión de evidencia digital existente.
- **Evidencia:** Capturas de pantalla de conversaciones utilizadas como parte del proceso actual de coordinación.

### Evidencia gráfica
## Foto sacada justo después de la entrevista por miembro del grupo.

<img width="720" height="1280" alt="WhatsApp Image 2026-09-27 at 23 48 45" src="https://github.com/user-attachments/assets/b4e3f54c-02a7-48a7-8f09-bb7b531f0788" />


### Objetivo de la revisión

Analizar la forma en que actualmente se comunica y organiza información relacionada con los ensayos, para identificar problemas derivados del uso de herramientas de mensajería no especializadas para este proceso.

### Hallazgos principales

- La coordinación se realiza mediante conversaciones digitales que no poseen una estructura específica para gestionar ensayos.

- La información relacionada con una actividad puede quedar mezclada con otros mensajes de la conversación.

- No existe dentro de la conversación una estructura formal que relacione automáticamente a cada participante con el instrumento o rol que desempeñará durante el ensayo.

- Las respuestas y acuerdos deben ser interpretados por las personas responsables de la coordinación.

- La herramienta utilizada para comunicarse cumple principalmente una función de mensajería, pero no realiza automáticamente una evaluación de los integrantes o roles disponibles para un ensayo.

- La revisión respalda la necesidad de centralizar la convocatoria en un evento estructurado donde puedan registrarse explícitamente la asistencia y los roles de los integrantes.

- También se identifica la conveniencia de que la información de cada ensayo tenga un estado definido y pueda consultarse sin depender de buscar mensajes antiguos dentro de una conversación.

### Conclusiones de la revisión documental

La revisión de las conversaciones permite observar que el mecanismo actual facilita la comunicación entre los integrantes, pero no se encuentra diseñado específicamente para gestionar la convocatoria y confirmación de ensayos.

Esto obliga a que parte importante del proceso de organización, interpretación de respuestas y verificación de disponibilidad sea realizada manualmente.

La propuesta TO-BE busca reducir este problema mediante eventos estructurados, registro de asistencia e instrumentos, evaluación de las condiciones necesarias para realizar el ensayo y notificaciones asociadas al estado del evento.

---

## Acta de acuerdo

A partir de la entrevista y de la revisión de la información disponible, se establecen los siguientes acuerdos y necesidades principales:

1. La solución deberá permitir crear convocatorias de ensayo de forma estructurada.

2. Cada integrante deberá poder indicar su disponibilidad para participar.

3. Un integrante podrá indicar uno o múltiples instrumentos o roles musicales con los que puede participar.

4. La evaluación de la viabilidad de un ensayo deberá considerar los roles musicales requeridos y no únicamente la cantidad total de personas disponibles.

5. Los músicos base identificados durante la entrevista son teclado, bajo, guitarra y batería.

6. La ausencia de un músico base deberá ser visible para las personas responsables de la coordinación.

7. Cuando no se encuentren cubiertas las condiciones necesarias para el ensayo, el sistema deberá apoyar la decisión de esperar nuevas confirmaciones o reagendar.

8. El encargado y el director musical poseen responsabilidades relevantes dentro del proceso de organización y toma de decisiones.

9. El sistema deberá disminuir la dependencia de mensajes dispersos para conocer el estado actual de una convocatoria.

10. Las decisiones y requisitos obtenidos mediante la elicitación servirán como base para definir y validar el proceso TO-BE, los requisitos de producto y las historias de usuario.
