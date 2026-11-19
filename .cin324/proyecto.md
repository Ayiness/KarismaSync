# Estado del proyecto — generación de la aplicación

## Proyecto
- Nombre: KarismaSync
- Repositorio de documentación: esta carpeta
- Última auditoría: 2026-11-18 — verificación rápida; se agregó HU-07

## Mapa de artefactos (rutas detectadas)
| Artefacto | Ruta(s) | Estado |
|-----------|---------|--------|
| BPMN AS-IS | `01-proceso-as-is.md`, `diagramas/AS-IS.bpmn` | completo |
| BPMN TO-BE | `02-rediseno-to-be.md`, `diagramas/TO-BE.bpmn` | completo |
| Historias de usuario | `04-historias-usuario.md` (HU-01 a HU-05) | completo |
| Criterios Gherkin | `07-criterios-aceptacion.md` | completo |
| Modelo de dominio | `08-modelo-dominio.md`, `diagramas/modelo-dominio.drawio`, `diagramas/modelo-dominio.png` | completo |
| Casos de uso | `09-casos-de-uso.md`, `diagramas/casos-de-uso.puml`, `diagramas/casos-de-uso.png` | parcial (solo CU-01 y CU-02) |
| Diagramas de estado | `11-diagramas-estado.md`, `diagramas/est-01.drawio`, `diagramas/est-01.png` | parcial (falta EST-02 como archivo) |
| Diagramas de secuencia | `10-diagramas-secuencia.md`, `diagramas/dss-01-crear-convocatoria.puml`, `diagramas/dss-02-verificar-viabilidad.puml` | completo (enlaces rotos en el índice) |
| Requisitos y atributos de calidad | `03-requisitos.md`, `06-atributos-calidad.md`, `12-trazabilidad.md` | requisitos completo; trazabilidad parcial |

## Supuestos acordados (por elementos faltantes o dudosos)
- 2026-11-05 — Confirmado por el estudiante: el enum `EstadoEvento` del modelo de dominio (`Vigente`, `Confirmado`, `Cancelado`, `Terminado`) es la fuente de verdad. «Condiciones pendientes» y «En espera» se modelan como evento `Vigente` con una `Alerta`.
- 2026-11-05 — Confirmado por el estudiante: HU-02, HU-03 y HU-05 no tienen caso de uso explícito; se deducen del TO-BE y del Gherkin. HU-03 activa la evaluación de HU-04 según `DSS-02`.
- 2026-11-05 — Confirmado por el estudiante: EST-02 (Asistencia) se toma de su tabla de transiciones en `11-diagramas-estado.md`; no existirá imagen `est-02`.
- 2026-11-05 — Confirmado por el estudiante: los enlaces rotos de `10-diagramas-secuencia.md` y la matriz desactualizada de `12-trazabilidad.md` quedan como deuda documental y no bloquean la generación.

## Stack (se define una sola vez)
- Lenguaje y framework: Python 3.12 + FastAPI + Jinja2
- Base de datos: SQLite — archivo `data/app.db`; migraciones SQL en `app/db/migrations/`
- Pruebas: pytest + TestClient de FastAPI
- Cómo instalar: `python -m venv .venv`; `.venv\Scripts\activate`; `pip install -r requirements.txt`
- Cómo ejecutar: `python -m app.db.seed`; `uvicorn app.main:app --reload` — URL: http://localhost:8000
- Cómo probar: `pytest`

## Historias
| Historia | Estado | Cambio de OpenSpec | Fecha | Observaciones |
|----------|--------|--------------------|-------|----------------|
| HU-01 | implementada, pendiente de validación del estudiante | `hu-01-crear-evento-ensayo` | 2026-11-05 | 14 pruebas en verde; notificaciones simuladas; falta probar a mano y archivar el cambio |
| HU-02 | pendiente | — | — | — |
| HU-03 | pendiente | — | — | — |
| HU-04 | pendiente | — | — | — |
| HU-05 | pendiente | — | — | — |
| HU-06 | implementada, pendiente de validación del estudiante | — | 2026-11-05 | perfil instrumental; pruebas en verde |
| HU-07 | implementada, pendiente de validación del estudiante | `hu-07-repertorio-opcional` | 2026-11-18 | repertorio opcional con 20 canciones de ejemplo; 27 pruebas en verde |

## Validaciones
| Historia | Informe | Estado | Fecha |
|----------|---------|--------|-------|

## Cambios posteriores
| Cambio | Historia afectada | Motivo | Fecha |
|--------|-------------------|--------|-------|
| `hu-07-repertorio-opcional` | HU-07 (nueva) | Repertorio de canciones opcional por evento, activado por defecto y con catálogo de 20 canciones | 2026-11-18 |
