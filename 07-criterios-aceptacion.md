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
    Y el quórum se propone en 6 integrantes
 
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
    Cuando Pedro informa que no asistirá al ensayo
    Entonces Pedro queda registrado como no asistente del ensayo
    Y no se registran instrumentos a su nombre para ese ensayo
 
  Escenario: El integrante intenta cambiar los instrumentos de su convocatoria
    Dado que Pedro fue convocado con guitarra eléctrica y voz
    Cuando Pedro intenta reemplazar guitarra eléctrica por guitarra acústica
    Entonces los instrumentos de su convocatoria no cambian
    Y Pedro es informado de que solo el Líder de Alabanza puede asignar los instrumentos
 
  Escenario: El integrante intenta confirmar después de que el evento fue cancelado
    Dado que el evento de ensayo del sábado 14 de noviembre fue cancelado
    Cuando Pedro intenta confirmar que asistirá con el instrumento bajo
    Entonces la asistencia de Pedro no queda registrada
    Y Pedro es informado de que la convocatoria ya no está disponible
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
 
