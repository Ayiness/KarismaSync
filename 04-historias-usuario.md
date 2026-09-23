# Historias de usuario

## HU-01: Convocatoria estructurada de ensayo
Como Líder de la banda, quiero publicar una propuesta de ensayo con fecha, hora y lugar en la plataforma, para evitar que los datos de coordinación se dispersen en mensajes informales de chat.

**Actividad TO-BE asociada:** Publicar propuesta de ensayo en la aplicación
**Criterios de aceptación:**
- CA1: El formulario debe validar obligatoriamente que la fecha sea posterior al momento de creación.
- CA2: El evento debe crearse inicialmente en estado "En votación".
- CA3: Inmediatamente tras la publicación, se debe disparar una notificación a todos los integrantes inscritos en la banda.

---

## HU-02: Votación de disponibilidad con asignación de rol instrumental
Como Integrante de la banda, quiero marcar mi asistencia ("Asisto" o "No asisto") y, en caso de asistir, indicar mi rol o instrumento (ej. Guitarra, Bajo, Batería, Teclado o Voz), para transparentar mi disponibilidad y especificar con qué rol musical participaré en la sesión.

**Actividad TO-BE asociada:** Registrar voto de asistencia en tarjeta/calendario
**Criterios de aceptación:**
- CA1: El usuario puede seleccionar solo una opción de asistencia ("Asisto" o "No asisto").
- CA2: Si el usuario marca "Asisto", el sistema debe desplegar de forma obligatoria un selector para indicar el rol o instrumento con el que asistirá.
- CA3: El usuario puede modificar su voto y su rol asignado mientras el periodo de votación permanezca abierto.
- CA4: El sistema debe mostrar el desglose en tiempo real de los integrantes confirmados diferenciando entre instrumentos y voces.

---

## HU-03: Validación automática de quórum con priorización instrumental
Como Líder de la banda, quiero que el sistema evalúe el quórum del 70% priorizando la presencia de integrantes con instrumentos sobre las voces, para asegurar que el ensayo cuente con la base instrumental indispensable antes de confirmarse.

**Actividad TO-BE asociada:** Calcular quórum de confirmación (Regla del 70% e instrumentos clave)
**Criterios de aceptación:**
- CA1: El sistema cambia automáticamente el estado del ensayo a "Confirmado" solo si se alcanza o supera el 70% de asistencia general y se cubre la presencia mínima requerida de instrumentos base.
- CA2: Si se alcanza el 70% de confirmaciones pero este porcentaje está compuesto mayoritariamente por voces y faltan instrumentos esenciales, el sistema no confirma el ensayo y marca el estado como "Quórum instrumental insuficiente".
- CA3: Si el quórum general no alcanza el 70% o no se cumple la base instrumental, el sistema envía una alerta automática al líder con el detalle de los roles faltantes y la opción directa para reagendar.

---

## HU-04: Recordatorio automático del ensayo
Como Integrante de la banda, quiero recibir una notificación automática el día del ensayo programado, para organizar mis tiempos y no olvidar mi asistencia a la sesión.

**Actividad TO-BE asociada:** Enviar notificación automática de recordatorio
**Criterios de aceptación:**
- CA1: La notificación solo se envía a los miembros del grupo si el ensayo está en estado "Confirmado".
- CA2: El recordatorio debe enviarse a la hora configurada (ej. 8:00 AM del día del ensayo o 2 horas antes de la sesión).
- CA3: Al pulsar la notificación, la app debe abrir la vista con los detalles del lugar y horario.

---

## HU-05: Bitácora y acuerdos técnicos post-ensayo
Como Líder de la banda, quiero registrar las canciones practicadas y las observaciones técnicas al finalizar el ensayo desglosadas por instrumento y voz, para mantener un registro claro de avances y compromisos que cada sección debe repasar.

**Actividad TO-BE asociada:** Registrar minuta, canciones ensayadas y observaciones
**Criterios de aceptación:**
- CA1: La opción de registrar minuta solo se habilita una vez que la hora de inicio del ensayo ha transcurrido.
- CA2: El formulario permite agregar múltiples temas musicales e ingresar acotaciones técnicas específicas por instrumento (ej. afinación/arreglos en guitarras, ritmo en batería o armonización en voces).
- CA3: La minuta debe quedar visible en el historial del evento para consulta de todos los integrantes.
