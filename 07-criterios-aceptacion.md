# Criterios de aceptación (Gherkin)
 
Los criterios se escriben a partir de las historias de [04-historias-usuario.md](./04-historias-usuario.md) y usan los términos del negocio: evento de ensayo, convocatoria, roles requeridos, asistencia, quórum y ensayo confirmado. En los escenarios, el quórum y los roles requeridos son datos del propio evento, definidos por el Líder de Alabanza al crear el evento y asignar instrumentos a cada músico convocado.
 
## HU-01 — Crear evento de ensayo con roles requeridos
 
Historia: Como Líder de Alabanza, quiero crear un evento de ensayo seleccionando qué músicos convocar y con qué instrumentos participará cada uno, para convocar solo a quienes se necesitan y definir los roles que cubrirá el evento.
 
```gherkin
Característica: Crear evento de ensayo con roles requeridos
 
  Escenario: La lista de convocados muestra a todos los músicos con su instrumento principal
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que la banda tiene 6 integrantes, cada uno con su instrumento principal
    Cuando Marta abre el formulario de creación de un evento de ensayo
    Entonces la lista muestra a los 6 integrantes convocados con su instrumento principal preseleccionado
    Y el campo de quórum aparece vacío para que Marta indique el quórum requerido
 
  Escenario: El líder crea un evento convocando a toda la banda
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que la banda tiene 6 integrantes, cada uno con su instrumento principal
    Cuando Marta crea un evento de ensayo para el sábado 14 de noviembre con un quórum de 6 integrantes y los 6 músicos convocados con sus instrumentos principales
    Entonces el evento de ensayo queda registrado como vigente con la fecha, el quórum y los roles que resultan de esos instrumentos
    Y los 6 integrantes de la banda reciben la convocatoria del evento
 
  Escenario: El líder convoca solo a los músicos que necesita
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que la lista de convocados muestra a los 6 integrantes con su instrumento principal
    Cuando Marta quita a Sofía y a Diego de la convocatoria del sábado 14 de noviembre
    Y crea el evento con un quórum de 4 integrantes y los 4 músicos restantes
    Entonces el evento de ensayo queda registrado como vigente con los roles que resultan de los instrumentos de los 4 convocados
    Y los 4 músicos convocados reciben la convocatoria del evento
    Y Sofía y Diego no reciben la convocatoria
 
  Escenario: El líder cambia o suma instrumentos a un músico convocado
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que Pedro está convocado con guitarra eléctrica como su instrumento principal
    Cuando Marta le asigna a Pedro guitarra acústica y voz para el ensayo del sábado 14 de noviembre
    Entonces guitarra acústica y voz quedan registrados como los instrumentos de Pedro en ese evento
    Y guitarra eléctrica no queda requerida por Pedro en ese evento
 
  Escenario: Un integrante sin rol de líder intenta crear un evento de ensayo
    Dado que Pedro es integrante de la banda y no tiene el rol de Líder de Alabanza
    Cuando Pedro intenta crear un evento de ensayo para el sábado 14 de noviembre
    Entonces el evento de ensayo no queda registrado
    Y ningún integrante recibe una convocatoria
    Y Pedro es informado de que solo el Líder de Alabanza puede crear eventos de ensayo
 
  Escenario: El líder intenta crear un evento de ensayo sin músicos convocados
    Dado que Marta tiene el rol de Líder de Alabanza
    Cuando Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin ningún músico convocado
    Entonces el evento de ensayo no queda registrado
    Y Marta es informada de que debe convocar al menos un músico
 
  Escenario: El líder intenta crear un evento con un músico convocado sin instrumentos
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que Ana está convocada sin ningún instrumento asignado
    Cuando Marta intenta crear un evento de ensayo para el sábado 14 de noviembre
    Entonces el evento de ensayo no queda registrado
    Y Marta es informada de que cada músico convocado debe tener al menos un instrumento

  Escenario: El líder intenta crear un evento de ensayo sin quórum
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que Pedro y Ana están convocados con sus instrumentos principales
    Cuando Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin indicar el quórum
    Entonces el evento de ensayo no queda registrado
    Y ningún integrante recibe una convocatoria
    Y Marta es informada de que debe indicar el quórum requerido

  Escenario: El líder intenta crear un evento con un quórum mayor que los músicos convocados
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que Marta, Pedro, Ana y Luis están convocados con sus instrumentos principales
    Cuando Marta intenta crear un evento de ensayo para el sábado 14 de noviembre con un quórum de 5 integrantes
    Entonces el evento de ensayo no queda registrado
    Y ningún integrante recibe una convocatoria
    Y Marta es informada de que el quórum no puede superar la cantidad de músicos convocados
```
 
## HU-02 — Acceder al evento desde la notificación
 
Historia: Como Integrante de la banda, quiero abrir la notificación recibida para acceder al evento de ensayo, para revisar la convocatoria y responder mientras siga vigente.
 
```gherkin
Característica: Acceder a la convocatoria de un evento de ensayo
 
  Escenario: El integrante accede a un evento de ensayo vigente
    Dado que Pedro recibió la convocatoria del ensayo del sábado 14 de noviembre
    Y que ese evento de ensayo está vigente
    Cuando Pedro accede al evento desde la convocatoria recibida
    Entonces Pedro conoce la fecha y los roles requeridos del ensayo
    Y Pedro puede registrar su asistencia al ensayo
 
  Escenario: El integrante intenta acceder a un evento de ensayo cancelado
    Dado que Pedro recibió la convocatoria del ensayo del sábado 14 de noviembre
    Y que ese evento de ensayo fue cancelado
    Cuando Pedro accede al evento desde la convocatoria recibida
    Entonces Pedro es informado de que la convocatoria ya no está disponible
    Y Pedro no puede registrar su asistencia al ensayo
 
  Escenario: El integrante intenta acceder a un evento de ensayo que ya terminó
    Dado que Pedro recibió la convocatoria del ensayo del sábado 7 de noviembre
    Y que ese evento de ensayo ya terminó
    Cuando Pedro accede al evento desde la convocatoria recibida
    Entonces Pedro es informado de que la convocatoria ya no está disponible
    Y Pedro no puede registrar su asistencia al ensayo
```
 
## HU-03 — Confirmar asistencia al ensayo
 
Historia: Como Integrante de la banda, quiero confirmar mi asistencia al ensayo y ver con qué instrumentos fui convocado, para saber cómo participaré.
 
```gherkin
Característica: Confirmar asistencia al ensayo
 
  Escenario: El integrante confirma su asistencia y ve los instrumentos asignados
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Pedro fue convocado con guitarra eléctrica y voz
    Cuando Pedro confirma que asistirá al ensayo
    Entonces Pedro queda registrado como asistente del ensayo
    Y guitarra eléctrica y voz quedan registrados como sus instrumentos para ese ensayo
    Y su respuesta queda considerada en la evaluación del quórum y de los roles requeridos
 
  Escenario: El integrante informa que no asistirá
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Pedro fue convocado con guitarra eléctrica
    Cuando Pedro informa que no asistirá al ensayo porque «tengo turno en el trabajo»
    Entonces Pedro queda registrado como no asistente del ensayo con el motivo «tengo turno en el trabajo»
    Y no se registran instrumentos a su nombre para ese ensayo

  Escenario: El integrante intenta informar que no asistirá sin indicar el motivo
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Pedro fue convocado con guitarra eléctrica
    Cuando Pedro informa que no asistirá al ensayo sin escribir un motivo
    Entonces la respuesta de Pedro no queda registrada y su asistencia sigue pendiente
    Y Pedro es informado de que debe indicar el motivo por el que no asistirá

  Escenario: El integrante cambia su respuesta de confirmada a no asiste
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Pedro confirmó su asistencia
    Cuando Pedro cambia su respuesta e informa que no asistirá porque «me enfermé»
    Entonces Pedro queda registrado como no asistente del ensayo con el motivo «me enfermé»

  Escenario: El integrante cambia su respuesta de no asiste a confirmada
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Pedro informó que no asistirá porque «tengo turno en el trabajo»
    Cuando Pedro cambia su respuesta y confirma que asistirá
    Entonces Pedro queda registrado como asistente del ensayo
    Y el motivo «tengo turno en el trabajo» ya no queda registrado
 
  Escenario: El integrante intenta cambiar los instrumentos de su convocatoria
    Dado que Pedro fue convocado con guitarra eléctrica y voz
    Cuando Pedro intenta reemplazar guitarra eléctrica por guitarra acústica
    Entonces los instrumentos de su convocatoria no cambian
    Y Pedro es informado de que solo el Líder de Alabanza puede asignar los instrumentos
 
  Escenario: El integrante intenta confirmar después de que el evento fue cancelado
    Dado que el evento de ensayo del sábado 14 de noviembre fue cancelado
    Cuando Pedro intenta confirmar que asistirá
    Entonces la asistencia de Pedro no queda registrada
    Y Pedro es informado de que la convocatoria ya no está disponible

  Escenario: Un integrante no convocado abre el evento
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Sofía no fue convocada a ese evento
    Cuando Sofía abre el evento
    Entonces Sofía ve la fecha del ensayo
    Y Sofía no ve la opción de responder ni las respuestas de los convocados

  Escenario: Un integrante no convocado intenta confirmar su asistencia
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Sofía no fue convocada a ese evento
    Cuando Sofía intenta confirmar que asistirá
    Entonces la asistencia de Sofía no queda registrada
    Y Sofía es informada de que no fue convocada a este evento

  Escenario: El líder revisa el estado de las respuestas de los convocados
    Dado que Marta creó el evento del sábado 14 de noviembre convocando a Pedro, Ana y Luis
    Y que Pedro confirmó su asistencia
    Y que Ana informó que no asistirá porque «tengo turno en el trabajo»
    Y que Luis todavía no responde
    Cuando Marta abre el detalle del evento
    Entonces ve a Pedro con su instrumento y el estado Confirmada
    Y ve a Ana con su instrumento, el estado No asiste y el motivo «tengo turno en el trabajo»
    Y ve a Luis con su instrumento y el estado Pendiente

  Escenario: Un músico convocado revisa las respuestas sin ver los motivos de los demás
    Dado que Marta creó el evento del sábado 14 de noviembre convocando a Pedro, Ana y Luis
    Y que Ana informó que no asistirá porque «tengo turno en el trabajo»
    Cuando Luis abre el detalle del evento
    Entonces ve a Ana con su instrumento y el estado No asiste
    Y no ve el motivo de Ana
```
 
## HU-04 — Evaluar automáticamente el quórum y los roles requeridos
 
Historia: Como Líder de Alabanza, quiero que el sistema evalúe automáticamente si se completó el quórum y los roles requeridos, para saber si el ensayo puede confirmarse sin realizar un conteo manual.
 
```gherkin
Característica: Evaluar el quórum y los roles requeridos de un ensayo
 
  Escenario: Se completan el quórum y los roles requeridos y el ensayo se confirma
    Dado que el evento de ensayo del sábado 14 de noviembre requiere un quórum de 4 integrantes y los roles batería, bajo y voz
    Y que 3 integrantes confirmaron su asistencia cubriendo batería y bajo
    Cuando Pedro confirma que asistirá con el instrumento voz
    Entonces el ensayo queda oficialmente confirmado
    Y la fecha del ensayo queda bloqueada en la agenda de la banda
    Y los integrantes de la banda reciben el aviso de ensayo confirmado
 
  Escenario: Se completa el quórum pero falta un rol requerido
    Dado que el evento de ensayo del sábado 14 de noviembre requiere un quórum de 4 integrantes y los roles batería, bajo y voz
    Y que 3 integrantes confirmaron su asistencia cubriendo bajo y voz
    Cuando Pedro confirma que asistirá con el instrumento guitarra
    Entonces el ensayo no queda confirmado
    Y el Líder de Alabanza recibe una alerta indicando que falta el rol batería
 
  Escenario: Todavía no se completa el quórum
    Dado que el evento de ensayo del sábado 14 de noviembre requiere un quórum de 4 integrantes y los roles batería y voz
    Y que 1 integrante confirmó su asistencia cubriendo batería
    Cuando Pedro confirma que asistirá con el instrumento voz
    Entonces el ensayo no queda confirmado
    Y el Líder de Alabanza recibe una alerta indicando que faltan 2 integrantes para completar el quórum
```
 
## HU-05 — Decidir acción cuando falta quórum o roles
 
Historia: Como Líder de Alabanza, quiero recibir una alerta cuando no se complete el quórum o falten roles requeridos, para decidir si espero nuevas confirmaciones o reagendo el ensayo.
 
```gherkin
Característica: Decidir qué hacer con un ensayo con condiciones pendientes
 
  Escenario: El líder decide esperar nuevas confirmaciones
    Dado que el ensayo del sábado 14 de noviembre tiene condiciones pendientes porque falta el rol batería
    Y que Marta, Líder de Alabanza, recibió la alerta de condiciones pendientes
    Cuando Marta decide mantener el ensayo en espera
    Entonces el ensayo sigue vigente y sin confirmar
    Y los integrantes pueden seguir registrando su asistencia
 
  Escenario: El líder decide reagendar el ensayo
    Dado que el ensayo del sábado 14 de noviembre tiene condiciones pendientes porque faltan 2 integrantes para el quórum
    Y que Marta, Líder de Alabanza, recibió la alerta de condiciones pendientes
    Cuando Marta reagenda el ensayo para el sábado 21 de noviembre
    Entonces el ensayo queda vigente con la nueva fecha y sin confirmar
    Y los integrantes de la banda reciben la convocatoria con la nueva fecha
 
  Escenario: El ensayo en espera no se confirma mientras sigan las condiciones pendientes
    Dado que el ensayo del sábado 14 de noviembre está en espera porque falta el rol batería
    Cuando Ana confirma que asistirá con el instrumento guitarra
    Entonces el ensayo no queda confirmado
    Y el Líder de Alabanza sigue informado de que falta el rol batería
```
 
## HU-06 — Registrar el perfil instrumental del integrante
 
Historia: Como Integrante de la banda, quiero registrar mi instrumento principal, para que el Líder de Alabanza sepa con qué instrumento convocarme a un ensayo.
 
```gherkin
Característica: Registrar el perfil instrumental del integrante
 
  Escenario: El integrante registra su instrumento principal
    Dado que Pedro es integrante de la banda y todavía no tiene un perfil instrumental
    Cuando Pedro selecciona guitarra eléctrica como su instrumento principal
    Entonces el perfil de Pedro queda registrado con guitarra eléctrica como instrumento principal
    Y el Líder de Alabanza puede ver ese instrumento al crear un evento de ensayo
 
  Escenario: El integrante cambia su instrumento principal
    Dado que Pedro tiene registrado guitarra eléctrica como su instrumento principal
    Cuando Pedro cambia su instrumento principal a guitarra acústica
    Entonces el perfil de Pedro queda con guitarra acústica como instrumento principal
 
  Escenario: El integrante intenta registrar su perfil sin instrumento principal
    Dado que Pedro es integrante de la banda y todavía no tiene un perfil instrumental
    Cuando Pedro intenta guardar su perfil sin indicar un instrumento principal
    Entonces el perfil de Pedro no queda registrado
    Y Pedro es informado de que debe indicar un instrumento principal
```
  
## HU-07 — Incluir un repertorio opcional de canciones en el evento
  
Historia: Como Líder de Alabanza, quiero incluir opcionalmente canciones en un evento, para preparar el repertorio cuando el evento sea un ensayo y omitirlo cuando sea una reunión u otra actividad.
  
```gherkin
Característica: Incluir un repertorio opcional de canciones en el evento
  
  Escenario: El formulario ofrece el repertorio activado por defecto con el catálogo de canciones
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que el catálogo de la banda tiene 20 canciones de ejemplo
    Cuando Marta abre el formulario de creación de un evento de ensayo
    Entonces el bloque de repertorio aparece activado por defecto
    Y Marta puede ver las 20 canciones del catálogo para seleccionarlas
  
  Escenario: El líder crea un evento con canciones seleccionadas
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que el catálogo de la banda tiene las canciones "Cuán grande es Él" y "Sublime gracia"
    Cuando Marta crea un evento de ensayo para el sábado 14 de noviembre y selecciona esas dos canciones
    Entonces el evento queda registrado con esas dos canciones en su repertorio
    Y el detalle del evento muestra las canciones seleccionadas
  
  Escenario: El líder crea un evento sin repertorio porque es una reunión
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que Marta está creando un evento para una reunión de coordinación
    Cuando Marta desactiva el bloque de repertorio y crea el evento para el sábado 14 de noviembre
    Entonces el evento queda registrado sin canciones
    Y el detalle del evento indica que no incluye repertorio
  
  Escenario: El líder deja el repertorio activado pero no selecciona canciones
    Dado que Marta tiene el rol de Líder de Alabanza
    Cuando Marta crea un evento para el sábado 14 de noviembre con el bloque de repertorio activado y sin seleccionar canciones
    Entonces el evento queda registrado sin canciones
    Y el detalle del evento indica que no incluye repertorio
  
  Escenario: Las canciones no seleccionadas no se asocian al evento
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que el catálogo de la banda tiene las canciones "Cuán grande es Él" y "Sublime gracia"
    Cuando Marta selecciona solo "Cuán grande es Él" al crear el evento del sábado 14 de noviembre
    Entonces "Cuán grande es Él" queda en el repertorio del evento
    Y "Sublime gracia" no queda asociada al evento
```

## HU-08 — Confirmar la convocatoria de un evento masivo

Historia: Como Representante de músicos, quiero revisar las convocatorias de eventos masivos que crea el Líder de Alabanza y aprobarlas o rechazarlas con una justificación, para que ningún evento masivo se publique a los músicos sin mi confirmación.

```gherkin
Característica: Confirmar la convocatoria de un evento masivo

  Escenario: El representante solo ve los eventos masivos pendientes de su banda
    Dado que Andrés tiene el rol de Representante de músicos de la banda
    Y que Marta creó un evento masivo para el sábado 12 de diciembre y un ensayo para el sábado 5 de diciembre
    Cuando Andrés abre las convocatorias por revisar
    Entonces ve el evento masivo del sábado 12 de diciembre como pendiente de aprobación
    Y no ve el ensayo del sábado 5 de diciembre

  Escenario: El representante aprueba un evento masivo
    Dado que el evento masivo del sábado 12 de diciembre está pendiente de aprobación
    Cuando Andrés, Representante de músicos, aprueba la convocatoria
    Entonces el evento queda vigente
    Y los músicos convocados reciben la convocatoria con su asistencia pendiente
    Y Marta, Líder de Alabanza, recibe el aviso de que el evento fue aprobado

  Escenario: El representante rechaza un evento masivo con justificación
    Dado que el evento masivo del sábado 12 de diciembre está pendiente de aprobación
    Cuando Andrés rechaza la convocatoria con la justificación "Coincide con el concierto regional"
    Entonces el evento queda rechazado
    Y los músicos convocados no reciben la convocatoria
    Y Marta recibe el rechazo con la justificación "Coincide con el concierto regional"

  Escenario: El representante intenta rechazar sin justificación
    Dado que el evento masivo del sábado 12 de diciembre está pendiente de aprobación
    Cuando Andrés rechaza la convocatoria sin escribir una justificación
    Entonces el sistema no registra el rechazo e informa que debe indicar la justificación
    Y el evento sigue pendiente de aprobación

  Escenario: El representante intenta revisar un evento ya aprobado
    Dado que el evento masivo del sábado 12 de diciembre ya fue aprobado
    Cuando Andrés intenta rechazarlo
    Entonces el sistema informa que el evento ya fue revisado
    Y el evento sigue vigente

  Escenario: El representante intenta crear un evento
    Dado que Andrés tiene el rol de Representante de músicos y no es Líder de Alabanza
    Cuando Andrés intenta crear un evento
    Entonces el sistema rechaza la solicitud por falta de permisos
    Y no se crea el evento

  Escenario: El líder intenta aprobar su propio evento masivo
    Dado que Marta, Líder de Alabanza, creó el evento masivo del sábado 12 de diciembre
    Cuando Marta intenta aprobar la convocatoria
    Entonces el sistema rechaza la solicitud por falta de permisos
    Y el evento sigue pendiente de aprobación
```

## HU-09 — Crear un evento masivo

Historia: Como Líder de Alabanza, quiero indicar que un evento es masivo al crearlo, para que el Representante de músicos confirme la convocatoria antes de que se publique a los convocados.

```gherkin
Característica: Crear un evento masivo

  Escenario: El formulario propone el tipo Ensayo por defecto
    Dado que Marta tiene el rol de Líder de Alabanza
    Cuando Marta abre el formulario de creación de un evento
    Entonces el tipo de evento aparece seleccionado como Ensayo
    Y Marta puede cambiarlo a Evento masivo

  Escenario: El líder crea un evento masivo que queda pendiente de aprobación
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que Andrés es el Representante de músicos de la banda
    Cuando Marta crea un evento masivo para el sábado 12 de diciembre con un quórum de 6 y 6 músicos convocados con sus instrumentos
    Entonces el evento queda pendiente de aprobación
    Y los músicos convocados no reciben la convocatoria
    Y Andrés recibe la solicitud de revisión del evento

  Escenario: El líder crea un ensayo y no pasa por revisión
    Dado que Marta tiene el rol de Líder de Alabanza
    Cuando Marta crea un evento de tipo Ensayo para el sábado 5 de diciembre con datos válidos
    Entonces el evento queda vigente
    Y los músicos convocados reciben la convocatoria

  Escenario: El líder intenta crear un evento masivo en una banda sin representante
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que la banda no tiene un Representante de músicos
    Cuando Marta intenta crear un evento masivo para el sábado 12 de diciembre
    Entonces el evento no se crea
    Y el sistema informa que la banda necesita un Representante de músicos

  Escenario: El evento masivo valida los mismos datos que un ensayo
    Dado que Marta tiene el rol de Líder de Alabanza
    Cuando Marta intenta crear un evento masivo sin quórum
    Entonces el evento no se crea
    Y el sistema informa que debe indicar el quórum
```
 
