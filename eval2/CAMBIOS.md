# Evaluación 2 — Cambio de requerimientos

> Plantilla preparada antes de la sesión. El martes 24/11 se completa **a mano, sin IA**, y cada fila la escribe su responsable.

## Equipo y responsables por artefacto

Una persona por artefacto (somos 4 para 6 artefactos, así que dos integrantes tienen dos). La responsabilidad es por artefacto, no por rol.

| Artefacto | Archivos | Responsable |
|-----------|----------|-------------|
| HU y Gherkin | `04-historias-usuario.md`, `07-criterios-aceptacion.md` | [confirmar] |
| Modelo de dominio | `08-modelo-dominio.md`, `diagramas/modelo-dominio.drawio` + `.png` | [confirmar] |
| Casos de uso | `09-casos-uso.md`, `diagramas/casos-de-uso.puml` + `.png` | [confirmar] |
| Diagramas de secuencia | `10-diagramas-secuencia.md`, `diagramas/dss-*.puml` + `.png` | [confirmar] |
| Diagramas de estado | `11-diagramas-estado.md`, `diagramas/est-*.puml`/`.drawio` + `.png` | [confirmar] |
| Matriz de trazabilidad | `12-trazabilidad.md` | [confirmar] |

## El cambio solicitado

**Enunciado del profesor (24/11):**
[copiar aquí el cambio tal como lo planteó el profesor]

**Cómo lo entendimos (con nuestras palabras, validado por el profesor):**
[explicación del equipo]

**Dudas resueltas en la sesión:**
- [pregunta → respuesta del profesor]

## Cambios por artefacto

Una fila por artefacto. Si un artefacto no cambia, se escribe «Sin cambios» y la razón.

| Artefacto | Qué cambió (antes → después, con identificadores) | Por qué el cambio solicitado lo exige | Responsable |
|-----------|---------------------------------------------------|---------------------------------------|-------------|
| HU y Gherkin | [p. ej. HU-0X CA2: «…» → «…»; nuevo escenario «…»] | | |
| Modelo de dominio | [p. ej. clase `X`: nuevo atributo `y: Tipo`; multiplicidad 0..1 → 1..*] | | |
| Casos de uso | [p. ej. CU-0X: nuevo flujo alternativo «…»] | | |
| Diagramas de secuencia | [p. ej. DSS-0X: nuevo mensaje `mensaje(param)`; nuevo bloque `alt` «…»] | | |
| Diagramas de estado | [p. ej. EST-01: nuevo estado `X`; transición `A --evento [guarda]--> B`] | | |
| Matriz de trazabilidad | [p. ej. nueva fila RF-XX → HU-0X → CU-0X → DSS-0X → EST-0X] | | |

## Correcciones posteriores (después de `cambio-validado`)

Se completa entre el martes y el jueves, al implementar con `/cin324-generar-app`. Sirve como evidencia para la reflexión.

| Artefacto | Qué se corrigió | Por qué faltaba o estaba mal (evidencia: commit, `design.md` del cambio `ajuste-…`, prueba fallida) |
|-----------|-----------------|------------------------------------------------------------------------------------------------------|
| | | |

## Etiquetas de Git

| Etiqueta | Momento | Contenido |
|----------|---------|-----------|
| `base-eval2` | antes del martes | 4 HU implementadas y artefactos consistentes con el código |
| `cambio-validado` | cierre de la sesión del martes | solo artefactos y este archivo |
| `entrega-eval2` | antes de la presentación del jueves | código, pruebas, cambio `ajuste-…` archivado y correcciones |
