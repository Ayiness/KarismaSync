# Estado del proyecto — generación de la aplicación

## Proyecto
- Nombre: KarismaSync
- Repositorio de documentación: esta carpeta
- Última auditoría: 2026-11-22 — orden previo a la Entrega 3: cambio OpenSpec de HU-06, DSS-03, trazabilidad HU→código→prueba, `.gitignore`

## Mapa de artefactos (rutas detectadas)
| Artefacto | Ruta(s) | Estado |
|-----------|---------|--------|
| BPMN AS-IS | `01-proceso-as-is.md`, `diagramas/AS-IS.bpmn` | completo |
| BPMN TO-BE | `02-rediseno-to-be.md`, `diagramas/TO-BE.bpmn` | completo |
| Historias de usuario | `04-historias-usuario.md` (HU-01 a HU-07) | completo |
| Criterios Gherkin | `07-criterios-aceptacion.md` | completo |
| Modelo de dominio | `08-modelo-dominio.md`, `diagramas/modelo-dominio.drawio`, `diagramas/modelo-dominio.png` | completo |
| Casos de uso | `09-casos-uso.md`, `diagramas/casos-de-uso.puml`, `diagramas/casos-de-uso.png` | CU-01 a CU-04 |
| Diagramas de estado | `11-diagramas-estado.md`, `diagramas/est-01.*`, `diagramas/est-02.puml`, `diagramas/est-02.png` | completo |
| Diagramas de secuencia | `10-diagramas-secuencia.md`, `diagramas/dss-01…04-*.puml` | completo (falta renderizar `dss-03-registrar-perfil-instrumental.png`) |
| Requisitos y atributos de calidad | `03-requisitos.md`, `06-atributos-calidad.md`, `12-trazabilidad.md` | completo; trazabilidad enlaza HU → código → prueba |

## Supuestos acordados (por elementos faltantes o dudosos)
- 2026-11-05 — Confirmado por el estudiante: el enum `EstadoEvento` del modelo de dominio (`Vigente`, `Confirmado`, `Cancelado`, `Terminado`) es la fuente de verdad. «Condiciones pendientes» y «En espera» se modelan como evento `Vigente` con una `Alerta`.
- 2026-11-05 — Confirmado por el estudiante: HU-02, HU-03 y HU-05 no tienen caso de uso explícito; se deducen del TO-BE y del Gherkin. HU-03 activa la evaluación de HU-04 según `DSS-02`.
- 2026-11-05 — EST-02 (Asistencia) se toma de su tabla de transiciones en `11-diagramas-estado.md`. (2026-11-22: ya existen `est-02.puml` y `est-02.png`.)
- 2026-11-05 — Los enlaces rotos de `10-diagramas-secuencia.md` y la matriz de `12-trazabilidad.md` quedaron como deuda documental. (2026-11-22: corregidos.)

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
| HU-06 | implementada, pendiente de validación del estudiante | `hu-06-perfil-instrumental` | 2026-11-05 | cambio de OpenSpec creado el 2026-11-22 para documentarla; pruebas separadas por escenario en `test_hu06_perfil_instrumental.py` |
| HU-07 | implementada, pendiente de validación del estudiante | `hu-07-repertorio-opcional` | 2026-11-18 | repertorio opcional con 20 canciones de ejemplo; 27 pruebas en verde |

## Validaciones
| Historia | Informe | Estado | Fecha |
|----------|---------|--------|-------|

## Cambios posteriores
| Cambio | Historia afectada | Motivo | Fecha |
|--------|-------------------|--------|-------|
| `hu-07-repertorio-opcional` | HU-07 (nueva) | Repertorio de canciones opcional por evento, activado por defecto y con catálogo de 20 canciones | 2026-11-18 |
| `hu-01-quorum-obligatorio` | HU-01 | El quórum es obligatorio (campo vacío en el formulario) y no puede superar a los convocados; la spec `eventos-ensayo` se alinea con el Gherkin vigente; DSS-01 corregido | 2026-11-23 |
