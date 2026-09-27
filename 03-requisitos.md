# Clasificación de requisitos

## Requisitos de producto

### Requisitos funcionales

| ID | Requisito | Tipo | Actividad TO-BE asociada |
|---|---|---|---|
| RF-01 | El sistema debe permitir al Líder de Alabanza crear un evento de ensayo indicando la fecha y los roles o instrumentos requeridos. | Funcional | Crear evento indicando fecha y roles requeridos |
| RF-02 | El sistema debe registrar el evento creado y notificar automáticamente a los integrantes de la banda sobre la nueva convocatoria. | Funcional | Registrar evento y notificar a la banda |
| RF-03 | El sistema debe permitir que un integrante acceda al evento correspondiente desde la notificación recibida. | Funcional | Abrir notificación para acceder al evento |
| RF-04 | El sistema debe verificar si el evento continúa vigente y no ha sido cancelado antes de permitir que un integrante registre su asistencia. | Funcional | Abrir notificación para acceder al evento / ¿El evento sigue vigente y no ha sido cancelado? |
| RF-05 | El sistema debe permitir a cada integrante confirmar su asistencia e indicar uno o múltiples instrumentos o roles con los que participará en el ensayo. | Funcional | Confirmar asistencia y seleccionar uno o múltiples instrumentos |
| RF-06 | El sistema debe registrar al músico y los instrumentos seleccionados dentro del evento correspondiente. | Funcional | Registrar músico e instrumentos en el evento |
| RF-07 | El sistema debe evaluar automáticamente si se completó el quórum y si se encuentran cubiertos los roles requeridos para el ensayo. | Funcional | ¿Se completó el quórum y los roles requeridos? |
| RF-08 | Si se cumplen las condiciones de quórum y roles requeridos, el sistema debe confirmar oficialmente el ensayo, bloquear la agenda correspondiente y notificar a los integrantes. | Funcional | Bloquear agenda y notificar ensayo oficial |
| RF-09 | Si no se completa el quórum o faltan roles requeridos, el sistema debe alertar al Líder de Alabanza e indicar que existen condiciones pendientes. | Funcional | Recibir alerta de sistema y decidir acción (esperar o re-agendar) |
| RF-10 | El sistema debe permitir al Líder de Alabanza decidir entre mantener el evento en espera de nuevas confirmaciones o reagendarlo cuando no se cumplan las condiciones requeridas. | Funcional | Recibir alerta de sistema y decidir acción (esperar o re-agendar) |
| RF-11 | Si el integrante intenta acceder a un evento que terminó o fue cancelado, el sistema debe informar que el evento ya no se encuentra disponible para registrar asistencia. | Funcional | ¿El evento sigue vigente y no ha sido cancelado? |

### Requisitos no funcionales

| ID | Requisito | Tipo | Actividad TO-BE asociada |
|---|---|---|---|
| RNF-01 | El sistema debe controlar el acceso según el rol del usuario, restringiendo la creación y reagendamiento de eventos al rol autorizado de Líder de Alabanza. | No funcional — Seguridad | Crear evento indicando fecha y roles requeridos / Recibir alerta de sistema y decidir acción |
| RNF-02 | La interfaz de confirmación debe permitir que un integrante registre su asistencia y seleccione sus instrumentos en un máximo de 15 segundos y con un máximo de 3 interacciones principales. | No funcional — Capacidad de interacción | Confirmar asistencia y seleccionar uno o múltiples instrumentos |
| RNF-03 | El registro de la asistencia y de los instrumentos seleccionados debe reflejarse en el sistema en menos de 1 segundo después de que el integrante confirme su respuesta. | No funcional — Eficiencia de desempeño | Registrar músico e instrumentos en el evento |
| RNF-04 | El servicio utilizado para notificar nuevas convocatorias y ensayos confirmados debe mantener una tasa de entrega exitosa de al menos 99,5 %. | No funcional — Fiabilidad | Registrar evento y notificar a la banda / Bloquear agenda y notificar ensayo oficial |
| RNF-05 | El sistema debe conservar el estado de asistencia y los instrumentos registrados utilizados para realizar la evaluación del quórum y de los roles requeridos. | No funcional — Fiabilidad | ¿Se completó el quórum y los roles requeridos? |

## Requisitos de proyecto

| ID | Requisito |
|---|---|
| RY-01 | El proyecto deberá contar con un equipo de desarrollo encargado de la implementación, pruebas y mantenimiento de la solución. |
| RY-02 | El proyecto deberá disponer de mecanismos de respaldo para proteger la información almacenada y permitir su recuperación ante fallos. |
| RY-03 | El proyecto deberá considerar recursos para el mantenimiento, actualización y corrección de errores después de la implementación. |
| RY-04 | El proyecto deberá considerar los costos asociados al alojamiento, almacenamiento y servicios necesarios para el funcionamiento de las notificaciones. |
| RY-05 | El proyecto deberá definir un responsable de supervisar las actividades de mantenimiento y soporte de la plataforma. |
| RY-06 | El proyecto deberá contemplar capacitación para las personas responsables de administrar y mantener la solución. |

## Requisito derivado

**Requisito origen:** RF-04 — El sistema debe verificar si el evento continúa vigente y no ha sido cancelado antes de permitir que un integrante registre su asistencia.

**Requisito derivado:** RD-01 — El sistema debe mantener un estado identificable para cada evento que permita distinguir, al menos, entre un evento vigente, cancelado o terminado.

**Justificación:** Para determinar si un integrante puede continuar al registro de asistencia, el sistema necesita conocer previamente el estado actual del evento. Sin esta información no sería posible ejecutar la decisión representada en el TO-BE por la compuerta “¿El evento sigue vigente y no ha sido cancelado?” ni impedir que se registren nuevas respuestas en convocatorias que ya finalizaron.
