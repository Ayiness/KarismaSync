# Clasificación de requisitos

## Requisitos de producto

### Requisitos Funcionales
| ID | Requisito | Actividad TO-BE asociada |
|:---|:---|:---|
| RF-01 | El sistema debe permitir al líder crear y convocar un ensayo ingresando fecha, hora de inicio/término y lugar. | Publicar propuesta de ensayo en la aplicación |
| RF-02 | El sistema debe emitir una notificación push automática a todos los integrantes de la banda al publicarse una nueva convocatoria. | Notificar convocatoria a los integrantes |
| RF-03 | El sistema debe permitir a cada integrante marcar su voto de asistencia ("Asisto" o "No asisto") y, en caso de asistir, seleccionar el rol instrumental con el que participará (ej. Guitarra, Bajo, Batería, Teclado o Voz). | Registrar voto de asistencia en tarjeta/calendario |
| RF-04 | El sistema debe calcular el quórum de confirmación evaluando que se alcance el 75% general y priorizando la presencia mínima de instrumentos base sobre la sección vocal. | Calcular quórum de confirmación (Regla del 75% e instrumentos clave) |
| RF-05 | El sistema debe confirmar el ensayo y fijarlo en el calendario de la banda de manera automática una vez validado el quórum del 70% y la cobertura instrumental requerida. | Notificar resultado de quórum y agendar/reagendar |
| RF-06 | El sistema debe notificar al líder en caso de no alcanzar el quórum general o faltar roles instrumentales prioritarios, habilitando la opción directa de reagendar. | Notificar resultado de quórum y agendar/reagendar |
| RF-07 | El sistema debe enviar una notificación automática de recordatorio el día del ensayo a los integrantes confirmados. | Enviar notificación automática de recordatorio |
| RF-08 | El sistema debe permitir al líder ingresar y guardar la minuta técnica post-ensayo con las canciones practicadas y las observaciones de arreglos/interpretación por instrumento. | Registrar minuta, canciones ensayadas y observaciones |
| RF-09 | El sistema debe desplegar a todos los miembros de la banda el historial de ensayos anteriores con sus acuerdos y canciones registradas. | Registrar minuta, canciones ensayadas y observaciones |

### Requisitos No Funcionales
| ID | Requisito | Actividad TO-BE asociada |
|:---|:---|:---|
| RNF-01 | El sistema debe actualizar el porcentaje de quórum y la distribución de instrumentos confirmados en menos de 1 segundo en la interfaz. | Registrar voto de asistencia en tarjeta/calendario |
| RNF-02 | El sistema debe controlar el acceso por roles, restringiendo la convocatoria de ensayos, reagendamiento y carga de minutas exclusivamente al rol "Líder". | Publicar propuesta de ensayo en la aplicación |
| RNF-03 | La interfaz de votación de KarismaSync debe permitir a un músico registrar su asistencia y elegir su instrumento en menos de 15 segundos y con un máximo de 3 toques en pantalla. | Registrar voto de asistencia en tarjeta/calendario |
| RNF-04 | El servicio de mensajería de notificaciones push debe garantizar una tasa de entrega exitosa de al menos un 99.5% hacia los dispositivos de los integrantes. | Enviar notificación automática de recordatorio |
| RNF-05 | Los recordatorios programados para el día del ensayo deben despacharse con un margen de desfase no mayor a ±1 minuto respecto al horario establecido. | Enviar notificación automática de recordatorio |
| RNF-06 | El sistema debe almacenar de forma inmutable el registro de quórum e instrumentos confirmados al momento del cierre de la votación. | Calcular quórum de confirmación (Regla del 70% e instrumentos clave) |
## Requisitos de proyecto

...

## Requisito derivado
**Requisito origen:** RF-04 (El sistema KarismaSync debe calcular automáticamente si los votos positivos alcanzan o superan el umbral del 70% del total de integrantes activos).

**Justificación:** Para que el software pueda determinar matemáticamente si el ensayo se confirma o si se debe notificar al líder para reagendar antes del día del evento, es indispensable contar con una regla temporal de cierre; de lo contrario, si un integrante no vota, la sesión quedaría bloqueada en estado indefinido.
