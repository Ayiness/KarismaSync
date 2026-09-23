# Análisis de rediseño y propuesta TO-BE

## Mejoras identificadas por participante
| Participante | Objetivo | Problema | Mejora deseada |
|----------------|----------|----------|-----------------|
| Líder de Banda | Confirmar ensayos con asistencia suficiente sin desgaste operativo. | Desglose manual de respuestas e incertidumbre sobre el quórum real. | Automatización del cálculo de quórum (al menos 70%) y alerta inmediata si se requiere reagendar. |
| Líder de Banda | Mantener una bitácora técnica de avances. | Los acuerdos tomados se olvidan entre semanas. | Formulario centralizado para publicar canciones practicadas y observaciones técnicas por ensayo. |
| Integrante | Saber con certeza fecha, lugar y repertorio a repasar. | Pérdida de mensajes en el chat y falta de recordatorios. | Vista de calendario centralizada con votación en un clic y recordatorios push automáticos. |

## Iniciativas de rediseño

### Iniciativa 1: Automatización de la Evaluación de Quórum
- **Actividad(es) del AS-IS que afecta:** Conteo manual de respuestas por el líder en el chat de WhatsApp.
- **Heurística aplicada:** *Automatización de tareas* y *Reducción de variabilidad*.
- **Objetivo o mejora que resuelve:** Elimina el sesgo y tiempo invertido por el líder en contabilizar mensajes; la plataforma evalúa automáticamente el umbral del 70%.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):** 
  - **Tiempo:** Reduce de horas/días a segundos la verificación del quórum una vez cerrado el plazo.
  - **Calidad:** Elimina errores humanos y ambigüedades en la confirmación.

### Iniciativa 2: Centralización de Eventos y Notificaciones Push
- **Actividad(es) del AS-IS que afecta:** Notificación manual mediante mensajes de texto y verificación dispersa de la fecha.
- **Heurística aplicada:** *Centralización de información (Integration)* y *Notificación proactiva por excepción*.
- **Objetivo o mejora que resuelve:** Proporciona un calendario interactivo único y notificaciones dirigidas (convocatoria, recordatorio de votación, confirmación y recordatorio el día del evento).
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Calidad:** Disminuye drásticamente la tasa de inasistencia u olvido por parte de los músicos.
  - **Flexibilidad:** El líder visualiza el estado en tiempo real.

### Iniciativa 3: Digitalización y Persistencia de la Bitácora Musical
- **Actividad(es) del AS-IS que afecta:** Anotaciones personales o comunicación verbal de acuerdos post-ensayo.
- **Heurística aplicada:** *Enriquecimiento de información*.
- **Objetivo o mejora que resuelve:** Registrar y asociar canciones ensayadas y observaciones técnicas al evento ejecutado.
- **Efecto esperado (tiempo/costo/calidad/flexibilidad):**
  - **Calidad:** Mejora sustancial en la preparación técnica de los músicos para futuras presentaciones.

## Diagrama TO-BE
![Proceso TO-BE](./diagramas/to-be.png)

Archivo fuente: [`./diagramas/to-be.bpmn`](./diagramas/to-be.bpmn)

*Tipos de tareas representadas:*
- **User Task:** "Publicar propuesta de ensayo" (Líder), "Votar disponibilidad" (Integrante), "Registrar minuta y acuerdos" (Líder).
- **Service Task:** "Enviar notificación push de convocatoria" (Sistema), "Calcular quórum del 70%" (Sistema), "Confirmar y agendar evento en calendario" (Sistema), "Emitir recordatorio automático del ensayo" (Sistema).
- **Manual Task:** "Ejecutar sesión de ensayo presencial" (Líder e Integrantes).

## Actividades que cambian del AS-IS al TO-BE
| Actividad en el AS-IS | Actividad en el TO-BE | Qué cambia |
|-------------------------|--------------------------|------------|
| Redactar y enviar mensaje con fecha en WhatsApp | Publicar propuesta de ensayo en la aplicación | Pasa de un mensaje de texto libre a un formulario estructurado con fecha, hora de inicio/término y lugar. |
| Leer mensajes y enviar confirmación por texto/emoji | Registrar voto de asistencia en tarjeta/calendario | Los integrantes responden mediante botones discretos ("Asisto" / "No asisto") dentro del sistema. |
| Contar manualmente las respuestas en el chat grupal | Calcular quórum de confirmación (Regla del 70%) | El sistema ejecuta una tarea de servicio automática calculando si los votos positivos superan o igualan el 70%. |
| Acordar informalmente o cancelar por falta de respuesta | Notificar resultado de quórum y agendar/reagendar | Si cumple, el sistema agenda automáticamente y notifica la confirmación; si no, notifica al líder para reagendar con una nueva fecha. |
| Recordar verbalmente el ensayo o preguntar en el grupo | Enviar notificación automática de recordatorio | El sistema despacha notificaciones automáticas previas al evento y el mismo día del ensayo. |
| Acordar de palabra o en chats qué canciones se practicaron | Registrar minuta, canciones ensayadas y observaciones | El líder completa un módulo post-ensayo adjuntando repertorio trabajado y notas de interpretación. |
