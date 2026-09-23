# Proceso de negocio — AS-IS

## Macro-proceso y proceso específico
Gestión Operativa de Bandas Musicales → Convocatoria, confirmación y registro de ensayos mediante mensajería instantánea (WhatsApp).

## Objetivo de negocio del proceso
Coordinar la fecha, hora, lugar y contenido técnico de las sesiones de ensayo, asegurando la asistencia suficiente de los integrantes para un ensayo productivo.

## Participantes y sus objetivos
| Participante | Objetivo en el proceso |
|---------------|------------------------|
| Líder de Banda / Director Musical | Fijar oportunamente una sesión con quórum suficiente y dejar constancia de los acuerdos musicales tomados. |
| Integrante / Músico | Conocer con claridad los datos del ensayo (cuándo y dónde), manifestar disponibilidad fácilmente y acceder al repertorio acordado. |

## Diagrama AS-IS
![Proceso AS-IS](./diagramas/as-is.png)

Archivo fuente: [`./diagramas/as-is.bpmn`](./diagramas/as-is.bpmn)



## Problemas identificados
- **Dilución y pérdida de información:** Los mensajes con propuestas de fechas y lugares se pierden entre conversaciones informales, stickers y audios dentro del grupo de WhatsApp.
- **Conteo manual y ambiguo de quórum:** El líder debe contar manualmente respuestas informales (emojis, textos ambiguos, silencios), produciendo incertidumbre sobre si el grupo alcanzará la asistencia mínima necesaria.
- **Falta de trazabilidad de acuerdos y repertorio:** Los temas ensayados, notas de afinación y compromisos quedan en la memoria de los músicos o en audios sueltos, provocando olvidos y retrocesos en el siguiente ensayo.
- **Ausencia de recordatorios estructurados:** Los integrantes olvidan asistir o llegar a la hora por no contar con una alerta vinculada a un calendario formal.
