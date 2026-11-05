# Criterios de aceptación (Gherkin)
 
Los criterios se escriben a partir de las historias de [04-historias-usuario.md](./04-historias-usuario.md) y usan los términos del negocio: evento de ensayo, convocatoria, roles requeridos, asistencia, quórum y ensayo confirmado. En los escenarios, el quórum y los roles requeridos son datos del propio evento, definidos por el Líder de Alabanza al crearlo.
 
## HU-01 — Crear evento de ensayo con roles requeridos
 
Historia: Como Líder de Alabanza, quiero crear un evento de ensayo indicando la fecha y los roles requeridos, para organizar la convocatoria y definir qué músicos son necesarios para realizar el ensayo.
 
```gherkin
Característica: Crear evento de ensayo con roles requeridos
 
  Escenario: El líder crea un evento de ensayo y la banda es convocada
    Dado que Marta tiene el rol de Líder de Alabanza
    Y que la banda tiene 6 integrantes
    Cuando Marta crea un evento de ensayo para el sábado 14 de noviembre con los roles requeridos batería, bajo, guitarra y voz
    Entonces el evento de ensayo queda registrado como vigente con la fecha y los roles requeridos indicados
    Y los 6 integrantes de la banda reciben la convocatoria del evento
 
  Escenario: Un integrante sin rol de líder intenta crear un evento de ensayo
    Dado que Pedro es integrante de la banda y no tiene el rol de Líder de Alabanza
    Cuando Pedro intenta crear un evento de ensayo para el sábado 14 de noviembre
    Entonces el evento de ensayo no queda registrado
    Y ningún integrante recibe una convocatoria
    Y Pedro es informado de que solo el Líder de Alabanza puede crear eventos de ensayo
 
  Escenario: El líder intenta crear un evento de ensayo sin roles requeridos
    Dado que Marta tiene el rol de Líder de Alabanza
    Cuando Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin indicar roles requeridos
    Entonces el evento de ensayo no queda registrado
    Y Marta es informada de que debe indicar al menos un rol requerido
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
 
## HU-03 — Confirmar asistencia y seleccionar instrumentos
 
Historia: Como Integrante de la banda, quiero confirmar mi asistencia e indicar uno o múltiples instrumentos con los que participaré, para que el sistema registre correctamente mi disponibilidad y aporte musical al ensayo.
 
```gherkin
Característica: Confirmar asistencia e instrumentos a un ensayo
 
  Escenario: El integrante confirma su asistencia con más de un instrumento
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Y que Pedro todavía no ha registrado su asistencia
    Cuando Pedro confirma que asistirá con los instrumentos guitarra y voz
    Entonces Pedro queda registrado como asistente del ensayo
    Y guitarra y voz quedan registrados como sus instrumentos para ese ensayo
    Y su respuesta queda considerada en la evaluación del quórum y de los roles requeridos
 
  Escenario: El integrante informa que no asistirá
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Cuando Pedro informa que no asistirá al ensayo
    Entonces Pedro queda registrado como no asistente del ensayo
    Y no se registran instrumentos a su nombre para ese ensayo
 
  Escenario: El integrante confirma su asistencia sin indicar instrumentos
    Dado que el evento de ensayo del sábado 14 de noviembre está vigente
    Cuando Pedro confirma que asistirá sin indicar ningún instrumento
    Entonces la asistencia de Pedro no queda registrada
    Y Pedro es informado de que debe indicar al menos un instrumento o rol
 
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
 
