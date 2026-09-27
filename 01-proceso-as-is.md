# Proceso de negocio — AS-IS

## Macro-proceso y proceso específico

Gestión Operativa de la Agrupación Musical → Coordinación y confirmación de ensayos mediante comunicación informal, principalmente a través de WhatsApp o reuniones presenciales.

## Objetivo de negocio del proceso

Coordinar la realización de un ensayo, comunicando una propuesta a los integrantes, recopilando sus respuestas de asistencia y determinando si existe disponibilidad suficiente para llevarlo a cabo.

## Participantes y sus objetivos

| Participante | Objetivo en el proceso |
|---|---|
| Líder de Alabanza | Proponer y coordinar oportunamente un ensayo, conocer la disponibilidad de los músicos y determinar si existen suficientes integrantes para realizarlo. |
| Integrante de la banda | Recibir la propuesta del ensayo y comunicar si podrá o no asistir. |

## Diagrama AS-IS

[Proceso AS-IS]<img width="1437" height="644" alt="Proceso AS-IS" src="https://github.com/user-attachments/assets/4f05ffd8-fd06-476d-829f-d5889a776f7c" />

Archivo fuente editable: [`AS-IS.bpmn`](./diagramas/AS-IS.bpmn)

## Tipos de tareas representadas

### User Task
Actividades realizadas por una persona utilizando una herramienta digital como WhatsApp:

- **Proponer ensayo por WhatsApp o en reunión dominical:** el Líder de Alabanza comunica la intención de realizar un ensayo.
- **Responder confirmando asistencia o inasistencia:** los integrantes comunican su disponibilidad.
- **Cancelar ensayo o volver a preguntar:** el líder comunica la decisión cuando no existe disponibilidad suficiente.

### Manual Task
Actividades realizadas por una persona sin automatización del sistema:

- **Realizar el ensayo presencial:** los integrantes ejecutan físicamente la sesión de ensayo una vez confirmada.

### Service Task
En el proceso AS-IS no existe actualmente una plataforma especializada que automatice la evaluación del quórum, el registro de instrumentos o la confirmación del ensayo. Estas automatizaciones son incorporadas posteriormente en la propuesta TO-BE.

## Problemas identificados

- **Información dispersa:** La propuesta y las respuestas de asistencia quedan mezcladas con otros mensajes dentro del grupo de WhatsApp, dificultando encontrar rápidamente la información relevante.

- **Confirmaciones no estructuradas:** Los integrantes comunican su asistencia o inasistencia mediante mensajes informales, por lo que no existe un formato único para registrar la disponibilidad.

- **Evaluación manual del quórum:** El Líder de Alabanza debe revisar las respuestas recibidas y determinar manualmente si existen suficientes integrantes y roles musicales para realizar el ensayo.

- **Falta de información sobre los roles disponibles:** Una confirmación de asistencia no permite identificar de forma estructurada qué instrumento o rol musical cubrirá cada integrante.

- **Gestión manual cuando faltan integrantes:** Si no existen suficientes músicos disponibles, el líder debe decidir manualmente si espera nuevas respuestas, vuelve a preguntar o cancela el ensayo.
