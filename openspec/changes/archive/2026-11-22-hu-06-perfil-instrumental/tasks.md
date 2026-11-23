# Tasks — HU-06 Registrar el perfil instrumental del integrante

## 1. Base de datos y datos de ejemplo

- [x] 1.1 Crear la tabla `integrantes_instrumentos` en `app/db/migrations/002_perfil_y_convocados.sql`.
- [x] 1.2 Sembrar un instrumento principal de ejemplo por integrante en `app/db/seed.py`.

## 2. Rutas y pantallas

- [x] 2.1 Agregar `GET /perfil` con el catálogo de instrumentos y el instrumento actual.
- [x] 2.2 Agregar `POST /perfil` que registra o reemplaza el instrumento principal y rechaza el guardado sin instrumento.
- [x] 2.3 Mostrar el instrumento principal de cada integrante en el formulario de creación de eventos.

## 3. Pruebas de integración (escenarios Gherkin)

- [x] 3.1 «HU-06 · El integrante registra su instrumento principal» → `test_hu06_el_integrante_registra_su_instrumento_principal`.
- [x] 3.2 «HU-06 · El integrante cambia su instrumento principal» → `test_hu06_el_integrante_cambia_su_instrumento_principal`.
- [x] 3.3 «HU-06 · El integrante intenta registrar su perfil sin instrumento principal» → `test_hu06_el_integrante_intenta_registrar_su_perfil_sin_instrumento_principal`.

## 4. Documentación

- [x] 4.1 Agregar DSS-03 (`diagramas/dss-03-registrar-perfil-instrumental.puml`).
- [x] 4.2 Actualizar `README.md` y `12-trazabilidad.md`.
