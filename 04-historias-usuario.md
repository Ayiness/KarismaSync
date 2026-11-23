# Historias de usuario

## HU-01: Crear evento de ensayo con roles requeridos
Como Líder de Alabanza, quiero crear un evento de ensayo seleccionando qué músicos convocar y con qué instrumentos participará cada uno, para convocar solo a quienes se necesitan y definir los roles que cubrirá el evento.

**Actividad TO-BE asociada:** Crear evento convocando músicos y asignando sus instrumentos

**Criterios de aceptación:**
- CA1: El líder debe poder ingresar la fecha del ensayo.
- CA2: El sistema debe mostrar a todos los integrantes de la banda con su instrumento principal preseleccionado, y el líder debe poder quitar o volver a agregar músicos a la convocatoria.
- CA3: El líder debe poder asignar uno o más instrumentos a cada músico convocado, pudiendo reemplazar su instrumento principal por otro.
- CA4: El líder debe indicar el quórum requerido: un número de al menos 1 que no supere la cantidad de músicos convocados. El formulario no propone un valor y el evento no se crea sin quórum.
- CA5: Al crear el evento, el sistema debe registrarlo con los roles que resultan de los instrumentos asignados a los convocados.
- CA6: Al crear el evento, el sistema debe notificar solo a los músicos convocados.
- CA7: El evento debe quedar disponible para que los músicos convocados accedan a la convocatoria.
- CA8: No se debe crear el evento sin al menos un músico convocado con al menos un instrumento.

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

## HU-03: Confirmar asistencia al ensayo
Como Integrante de la banda, quiero confirmar mi asistencia al ensayo y ver con qué instrumentos fui convocado, para saber cómo participaré.

**Actividad TO-BE asociada:** Confirmar asistencia al ensayo

**Criterios de aceptación:**
- CA1: El integrante debe poder indicar si asistirá al ensayo.
- CA2: Si confirma su asistencia, el sistema debe mostrarle los instrumentos que el Líder de Alabanza le asignó.
- CA3: El sistema debe registrar la asistencia del músico y los instrumentos asignados en su convocatoria dentro del evento.
- CA4: La información registrada debe quedar disponible para la evaluación automática del quórum y de los roles requeridos.
- CA5: El integrante no debe poder cambiar los instrumentos de su convocatoria; solo el Líder de Alabanza los define al crear el evento.
- CA6: Si el integrante indica que no asistirá, debe escribir un motivo (obligatorio, máximo 200 caracteres); sin motivo la respuesta no se registra.
- CA7: Mientras el evento esté vigente, el integrante puede cambiar su respuesta: de Confirmada a No asiste, indicando el motivo, o de No asiste a Confirmada, con lo que se borra el motivo anterior.
- CA8: Solo los músicos convocados pueden responder. Un integrante no convocado puede ver el evento, pero no registrar asistencia ni ver las respuestas.
- CA9: El Líder de Alabanza y los músicos convocados deben ver, en el detalle del evento, a cada convocado con sus instrumentos y el estado de su respuesta (Pendiente, Confirmada o No asiste). El motivo de inasistencia es privado: solo lo ven el Líder de Alabanza y el propio integrante.

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

---

## HU-06: Registrar el perfil instrumental del integrante
Como Integrante de la banda, quiero registrar mi instrumento principal, para que el Líder de Alabanza sepa con qué instrumento convocarme a un ensayo.

**Actividad TO-BE asociada:** Registrar el perfil instrumental del integrante

**Criterios de aceptación:**
- CA1: El integrante debe poder seleccionar su instrumento principal del catálogo.
- CA2: El perfil no puede quedar registrado sin instrumento principal.
- CA3: El instrumento principal debe quedar disponible para el Líder de Alabanza al crear un evento de ensayo.
- CA4: El integrante debe poder cambiar su instrumento principal.

---

## HU-07: Incluir un repertorio opcional de canciones en el evento
Como Líder de Alabanza, quiero incluir opcionalmente canciones en un evento, para preparar el repertorio cuando el evento sea un ensayo y omitirlo cuando sea una reunión u otra actividad.

**Actividad TO-BE asociada:** Crear evento convocando músicos y asignando sus instrumentos (incluye el repertorio opcional de canciones)

**Criterios de aceptación:**
- CA1: Al abrir el formulario de creación, el bloque de repertorio debe mostrarse activado por defecto.
- CA2: El líder debe poder desactivar el bloque de repertorio, y el evento debe poder crearse sin canciones.
- CA3: El líder debe poder seleccionar cero o más canciones del catálogo; la selección de canciones no es obligatoria.
- CA4: El sistema debe registrar las canciones seleccionadas asociadas al evento.
- CA5: Las canciones que no fueron seleccionadas no deben quedar asociadas al evento.
- CA6: El detalle del evento debe mostrar el repertorio registrado o indicar que el evento no incluye canciones.
- CA7: El catálogo de canciones debe estar disponible para el líder al crear el evento, con al menos 20 canciones de ejemplo.
