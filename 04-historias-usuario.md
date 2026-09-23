# Historias de usuario

## HU-01: Convocatoria estructurada de ensayo
Como **Líder de la banda**, quiero **publicar una propuesta de ensayo con fecha, hora y lugar en la plataforma**, para **evitar que los datos de coordinación se dispersen en mensajes informales de chat**.
- **Actividad TO-BE asociada:** Publicar propuesta de ensayo en la aplicación
- **Criterios de aceptación:**
  - CA1: El formulario debe validar obligatoriamente que la fecha sea posterior al momento de creación.
  - CA2: El evento debe crearse inicialmente en estado "En votación".
  - CA3: Inmediatamente tras la publicación, se debe disparar una notificación a todos los integrantes inscritos en la banda.

---

## HU-02: Votación de disponibilidad
Como **Integrante de la banda**, quiero **marcar mi asistencia ("Asisto" o "No asisto") directamente desde el calendario o detalle de la propuesta**, para **transparentar mi disponibilidad de forma rápida y sin ambigüedades**.
- **Actividad TO-BE asociada:** Registrar voto de asistencia en tarjeta/calendario
- **Criterios de aceptación:**
  - CA1: El usuario sólo puede seleccionar una opción a la vez.
  - CA2: El usuario puede modificar su voto siempre y cuando la votación continúe abierta.
  - CA3: El sistema debe reflejar el conteo consolidado de quórum de forma visible para todos los miembros.

---

## HU-03: Validación automática de quórum
Como **Líder de la banda**, quiero **que el sistema evalúe automáticamente si se alcanzó el 70% de confirmación**, para **saber de inmediato si el ensayo queda confirmado o si debo seleccionar una nueva fecha**.
- **Actividad TO-BE asociada:** Calcular quórum de confirmación (Regla del 70%)
- **Criterios de aceptación:**
  - CA1: Si las confirmaciones representan $\ge 70\%$ del total de miembros convocados al cumplirse el plazo, el estado del ensayo cambia automáticamente a "Confirmado".
  - CA2: Si las confirmaciones son $< 70\%$, el estado pasa a "No confirmado / Requiere reagendamiento".
  - CA3: En caso de no alcanzar el quórum, el sistema debe emitir una notificación push exclusiva al líder con acceso directo para reagendar.

---

## HU-04: Recordatorio automático del ensayo
Como **Integrante de la banda**, quiero **recibir una notificación automática el día del ensayo programado**, para **organizar mis tiempos y no olvidar mi asistencia a la sesión**.
- **Actividad TO-BE asociada:** Enviar notificación automática de recordatorio
- **Criterios de aceptación:**
  - CA1: La notificación solo se envía a los miembros del grupo si el ensayo está en estado "Confirmado".
  - CA2: El recordatorio debe enviarse a la hora configurada (ej. 8:00 AM del día del ensayo o 2 horas antes de la sesión).
  - CA3: Al pulsar la notificación, la app debe abrir la vista con los detalles del lugar y horario.

---

## HU-05: Bitácora y acuerdos técnicos post-ensayo
Como **Líder de la banda**, quiero **registrar las canciones practicadas y las observaciones técnicas al finalizar el ensayo**, para **mantener un registro claro de avances y compromisos para el siguiente ensayo**.
- **Actividad TO-BE asociada:** Registrar minuta, canciones ensayadas y observaciones
- **Criterios de aceptación:**
  - CA1: La opción de registrar minuta solo se habilita una vez que la hora de inicio del ensayo ha transcurrido.
  - CA2: Debe permitir agregar múltiples temas musicales e ingresar un área de texto para acotaciones de interpretación o arreglos.
  - CA3: La minuta debe quedar visible en el historial del evento para consulta de todos los integrantes.
