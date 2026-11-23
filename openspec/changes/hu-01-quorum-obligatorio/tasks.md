# Tasks — HU-01 Quórum obligatorio y sincronización de la spec

## 1. Lógica

- [x] 1.1 En `crear_evento`, rechazar el quórum vacío, no numérico o menor que 1 con «debe indicar el quórum requerido».
- [x] 1.2 Rechazar un quórum mayor que la cantidad de convocados con «el quórum no puede superar la cantidad de músicos convocados».

## 2. Pantalla

- [x] 2.1 Mostrar el campo de quórum vacío en «Crear evento», conservando el valor escrito si hay error.

## 3. Pruebas (escenarios Gherkin)

- [x] 3.1 «HU-01 · La lista de convocados muestra a todos los músicos con su instrumento principal»: comprobar que el campo de quórum aparece vacío.
- [x] 3.2 «HU-01 · El líder intenta crear un evento de ensayo sin quórum» → `test_hu01_lider_sin_quorum_no_crea_evento`.
- [x] 3.3 «HU-01 · El líder intenta crear un evento con un quórum mayor que los músicos convocados» → `test_hu01_lider_con_quorum_mayor_que_convocados_no_crea_evento`.
- [x] 3.4 Reemplazar las pruebas que aceptaban el quórum vacío por `test_quorum_vacio_no_crea` y agregar `test_quorum_mayor_que_convocados_no_crea`.

## 4. Artefactos

- [x] 4.1 Actualizar HU-01 CA4, el Gherkin de HU-01, CU-01 y DSS-01.
- [x] 4.2 Actualizar `12-trazabilidad.md` y `.cin324/proyecto.md`.
- [ ] 4.3 Exportar `diagramas/dss-01-crear-convocatoria.png` desde el `.puml` actualizado.
