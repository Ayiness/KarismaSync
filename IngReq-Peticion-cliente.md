## Cambio solicitado: HU-07 — Repertorio opcional de canciones
Se implementó el repertorio opcional de canciones como una nueva historia, **HU-07**, sin modificar la historia **HU-01** ya generada.

## Comportamiento agregado
- Al crear un evento aparece el bloque **"Repertorio de canciones (opcional)"**.
- El bloque viene activado por defecto.
- Se puede desactivar o dejar sin canciones, y el evento se crea igual.
- Solo se asocian al evento las canciones seleccionadas.
- El detalle del evento muestra el repertorio o indica que no incluye canciones.
- El inicio muestra cuántas canciones tiene cada evento.

## Catálogo de ejemplo (20 canciones)
| #  | Canción                    |
|----|----------------------------|
| 1  | Cuán grande es Él          |
| 2  | Sublime gracia             |
| 3  | Santo, santo, santo        |
| 4  | Alabaré                    |
| 5  | Te alabaré mi buen Jesús   |
| 6  | Renuévame                  |
| 7  | Tu fidelidad               |
| 8  | Grande es tu amor          |
| 9  | Dios está aquí             |
| 10 | Levanto mis manos          |
| 11 | Abre mis ojos              |
| 12 | Eres mi todo               |
| 13 | Mi esperanza está en Jesús |
| 14 | Cristo vive                |
| 15 | Digno eres                 |
| 16 | Nadie como tú              |
| 17 | Tu gracia es suficiente    |
| 18 | Cantamos aleluya           |
| 19 | El amor de Dios            |
| 20 | Eres digno                 |

## Artefactos modificados y justificación

### 1. Elicitación y TO-BE
| Documento | Cambio | Justificación |
|-----------|--------|---------------|
| 05-elicitacion.md | Se agregó la "Técnica 3: Solicitud de cambio del cliente" (18-11-2026). | El repertorio opcional no venía de la entrevista original; así queda registrado el origen de HU-07. |
| 02-rediseno-to-be.md | Se agregó la Iniciativa 7: Repertorio opcional del evento y su fila en "Actividades que cambian". | La selección ocurre dentro de la tarea existente "Crear evento…", por lo que no fue necesario modificar el BPMN. |

### 2. Requisitos
| Documento | Cambio | Justificación |
|-----------|--------|---------------|
| 03-requisitos.md | Se agregó **RF-13**. | Es una nueva capacidad funcional: mostrar el bloque activado por defecto, permitir desactivarlo y registrar solo las canciones seleccionadas. |
| 06-atributos-calidad.md | Solo se agregó una nota, sin atributos ni métricas nuevas. | HU-07 refuerza la adecuación funcional y la flexibilidad ya priorizadas, y RNF-02 sigue cubriendo la interacción. No corresponde inventar un RNF específico. |

### 3. Historia y criterios de aceptación
| Documento | Cambio |
|-----------|--------|
| 04-historias-usuario.md | Se agregó HU-07 con 7 criterios de aceptación. |
| 07-criterios-aceptacion.md | Se agregaron los escenarios Gherkin de HU-07 (detalle abajo). |

Escenarios Gherkin de HU-07:
- El formulario muestra el repertorio activo y el catálogo de 20 canciones.
- Se crea un evento con canciones seleccionadas.
- Se crea un evento sin repertorio porque es una reunión.
- Se deja el bloque activo sin seleccionar canciones.
- Las canciones no seleccionadas no se asocian.

### 4. Modelo de dominio
| Documento | Cambio |
|-----------|--------|
| 08-modelo-dominio.md | Se agregó la clase `Cancion` (titulo, autor) y la asociación **incluye** entre `EventoDeEnsayo` y `Cancion`, con multiplicidad `0..*` a `0..*`. |
| diagramas/modelo-dominio.drawio y .png | Se actualizaron la clase y la asociación en el diagrama. |

> **Decisión de diseño:** no se agregó un atributo booleano tipo `incluyeRepertorio`. Un evento sin canciones ya representa el caso de una reunión, y "activado por defecto" es una decisión de interfaz, no un estado del dominio.

### 5. Casos de uso y secuencia
| Documento | Cambio | Justificación |
|-----------|--------|---------------|
| 09-casos-uso.md | Se agregó **CU-04: Incluir repertorio opcional al crear un evento**. | Nuevo caso de uso asociado a HU-07. |
| 10-diagramas-secuencia.md y diagramas/dss-04-seleccionar-repertorio.puml/.png | Se agregó **DSS-04**. | La selección de canciones es un flujo de interacción nuevo dentro de la creación del evento. |
| diagramas/casos-de-uso.puml/.png | Se agregaron CU-04 y CU-03. | CU-03 faltaba en el diagrama. |

### 6. Diagramas de estado y trazabilidad
| Documento | Cambio |
|-----------|--------|
| 11-diagramas-estado.md | No se cambiaron transiciones. Solo se agregó una nota: el repertorio es un dato opcional y no modifica el ciclo de vida del evento. |
| 12-trazabilidad.md | Se agregó la fila de trazabilidad de HU-07 (abajo). |

| Requisito | Historia | Caso de uso | DSS | Estado | Clases |
|-----------|----------|-------------|-----|--------|--------|
| RF-13 | HU-07 | CU-04 | DSS-04 | [sin estado] | EventoDeEnsayo, Cancion |
