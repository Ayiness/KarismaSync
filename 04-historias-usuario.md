# Historias de usuario

## HU-01: Crear evento de ensayo con roles requeridos
Como Líder de Alabanza, quiero crear un evento de ensayo indicando la fecha y los roles requeridos, para organizar la convocatoria y definir qué músicos son necesarios para realizar el ensayo.

**Actividad TO-BE asociada:** Crear evento indicando fecha y roles requeridos

**Criterios de aceptación:**
- CA1: El líder debe poder ingresar la fecha del ensayo.
- CA2: El líder debe poder indicar los roles o instrumentos requeridos para el ensayo.
- CA3: Al crear el evento, el sistema debe registrarlo y notificar a los integrantes de la banda.
- CA4: El evento debe quedar disponible para que los integrantes puedan acceder a la convocatoria.

---

## HU-02: Acceder al evento desde la notificación
Como Integrante de la banda, quiero abrir la notificación recibida para acceder al evento de ensayo, para revisar la convocatoria y responder mientras siga vigente.

**Actividad TO-BE asociada:** Abrir notificación para acceder al evento

**Criterios de aceptación:**
- CA1: Al abrir la notificación, el sistema debe dirigir al integrante al evento correspondiente.
- CA2: Antes de permitir la confirmación, el sistema debe verificar que el evento siga vigente y no haya sido cancelado.
- CA3: Si el evento está vigente, el integrante debe poder continuar al registro de asistencia.
- CA4: Si el evento terminó o fue cancelado, el sistema debe informar que la convocatoria ya no está disponible.

---

## HU-03: Confirmar asistencia y seleccionar instrumentos
Como Integrante de la banda, quiero confirmar mi asistencia e indicar uno o múltiples instrumentos con los que participaré, para que el sistema registre correctamente mi disponibilidad y aporte musical al ensayo.

**Actividad TO-BE asociada:** Confirmar asistencia y seleccionar uno o múltiples instrumentos

**Criterios de aceptación:**
- CA1: El integrante debe poder indicar si asistirá al ensayo.
- CA2: Si confirma su asistencia, debe poder seleccionar uno o múltiples instrumentos o roles.
- CA3: El sistema debe registrar al músico y los instrumentos seleccionados dentro del evento.
- CA4: La información registrada debe quedar disponible para la evaluación automática del quórum y de los roles requeridos.

---

## HU-04: Evaluar automáticamente el quórum y los roles requeridos
Como Líder de Alabanza, quiero que el sistema evalúe automáticamente si se completó el quórum y los roles requeridos, para saber si el ensayo puede confirmarse sin realizar un conteo manual.

**Actividad TO-BE asociada:** ¿Se completó el quórum y los roles requeridos?

**Criterios de aceptación:**
- CA1: El sistema debe evaluar la asistencia registrada y los instrumentos o roles asociados a los músicos confirmados.
- CA2: La evaluación debe considerar los roles requeridos definidos al crear el evento.
- CA3: Si se cumple el quórum y están cubiertos los roles requeridos, el sistema debe bloquear la agenda y notificar que el ensayo quedó oficialmente confirmado.
- CA4: Si no se cumple el quórum o faltan roles requeridos, el sistema debe derivar el evento al flujo de excepción para que el líder tome una decisión.

---

## HU-05: Decidir acción cuando falta quórum o roles
Como Líder de Alabanza, quiero recibir una alerta cuando no se complete el quórum o falten roles requeridos, para decidir si espero nuevas confirmaciones o reagendo el ensayo.

**Actividad TO-BE asociada:** Recibir alerta de sistema y decidir acción (esperar o re-agendar)

**Criterios de aceptación:**
- CA1: La alerta debe indicar que el quórum o los roles requeridos aún no están completos.
- CA2: El líder debe poder identificar qué condición impide confirmar el ensayo.
- CA3: El líder debe poder decidir entre mantener el evento en espera o reagendarlo.
- CA4: Mientras no se cumplan las condiciones de confirmación, el sistema no debe marcar el ensayo como oficialmente confirmado.
