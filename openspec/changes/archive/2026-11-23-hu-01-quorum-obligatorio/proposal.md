# Proposal — HU-01 Quórum obligatorio y sincronización de la spec

## Why

La spec vigente `eventos-ensayo` quedó con los escenarios de una versión antigua de HU-01 (roles requeridos indicados a mano y convocatoria a toda la banda), mientras que el Gherkin, el código y las pruebas ya siguen la versión actual (convocar músicos con sus instrumentos). Además, el código aceptaba un quórum vacío y lo reemplazaba por la cantidad de convocados, lo que contradice la regla acordada por el equipo: **el evento solo se crea con un quórum indicado por el líder**, y ese quórum no puede superar la cantidad de músicos convocados.

## What Changes

- El quórum es obligatorio: si falta, el evento no se crea y se informa «debe indicar el quórum requerido».
- El quórum no puede superar la cantidad de músicos convocados: se informa «el quórum no puede superar la cantidad de músicos convocados».
- El formulario «Crear evento» muestra el campo de quórum vacío (antes se precargaba con la cantidad de integrantes).
- La spec `eventos-ensayo` se alinea con los escenarios Gherkin actuales de HU-01.

## Capabilities

### Modified Capabilities
- `eventos-ensayo`: quórum obligatorio y acotado por los convocados; escenarios alineados con el Gherkin vigente.

## Impact

- Código: `app/servicios/crear_evento.py` (validación del quórum) y `app/templates/evento_form.html` (campo vacío).
- Pruebas: `test_hu01_lider_sin_quorum_no_crea_evento`, `test_hu01_lider_con_quorum_mayor_que_convocados_no_crea_evento`, `test_quorum_vacio_no_crea`, `test_quorum_mayor_que_convocados_no_crea`; se eliminan las pruebas que aceptaban el quórum vacío.
- Artefactos: `04-historias-usuario.md` (HU-01 CA4), `07-criterios-aceptacion.md` (HU-01: primer escenario y dos escenarios nuevos), `09-casos-uso.md` (CU-01 alternativas), DSS-01 (`crearEvento(fecha, quorum, convocados[integrante, instrumentos])` y rama `datosInvalidos`), `12-trazabilidad.md`.
- Sin cambios: modelo de dominio (`quorum` ya es atributo de `EventoDeEnsayo`), esquema SQLite (`quorum INTEGER NOT NULL CHECK (quorum >= 1)`), EST-01 y EST-02.
- Fuera de alcance: evaluación del quórum con las asistencias (HU-04).
- Trazabilidad: HU-01, RF-01, CU-01, DSS-01.
