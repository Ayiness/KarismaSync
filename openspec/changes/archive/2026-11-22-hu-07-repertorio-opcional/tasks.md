# Tasks — HU-07 Incluir un repertorio opcional de canciones en el evento

## 1. Base de datos y datos de ejemplo

- [x] 1.1 Escribir `app/db/migrations/003_canciones.sql` con las tablas `canciones` y `eventos_canciones`; verificar ejecutando el seed y consultando las tablas.
- [x] 1.2 Agregar a `app/db/seed.py` un catálogo idempotente de 20 canciones de ejemplo; verificar el conteo y que ejecutar el seed dos veces no duplique datos.

## 2. Lógica de creación del evento

- [x] 2.1 Extender `DatosNuevoEvento` y `crear_evento` para recibir `canciones_ids`, validar que existan, deduplicarlas e insertar solo las seleccionadas en `eventos_canciones`; verificar que un evento sin canciones siga creándose.
- [x] 2.2 Verificar que una canción inexistente impida la creación y que el repertorio no altere las validaciones de fecha, quórum, convocados e instrumentos.

## 3. Rutas y pantallas

- [x] 3.1 Agregar `GET /eventos/nuevo` el catálogo de canciones y el bloque de repertorio activado por defecto; verificar que el formulario muestre las 20 canciones.
- [x] 3.2 Procesar en `POST /eventos` el bloque `incluir_repertorio` y las canciones seleccionadas; si el bloque está desactivado, crear el evento sin canciones.
- [x] 3.3 Mostrar el repertorio en `GET /eventos/{id}` o el aviso de que el evento no incluye canciones; agregar el conteo de canciones al inicio.

## 4. Pruebas de integración (escenarios Gherkin)

- [x] 4.1 Escribir la prueba «HU-07 · El formulario ofrece el repertorio activado por defecto con el catálogo de canciones» y verificar que pase con `pytest`.
- [x] 4.2 Escribir la prueba «HU-07 · El líder crea un evento con canciones seleccionadas» y verificar que pase con `pytest`.
- [x] 4.3 Escribir la prueba «HU-07 · Las canciones no seleccionadas no se asocian al evento» y verificar que pase con `pytest`.
- [x] 4.4 Escribir la prueba «HU-07 · El líder crea un evento sin repertorio porque es una reunión» y verificar que pase con `pytest`.
- [x] 4.5 Escribir la prueba «HU-07 · El líder deja el repertorio activado pero no selecciona canciones» y verificar que pase con `pytest`.

## 5. Documentación

- [x] 5.1 Actualizar `README.md` con las 20 canciones de ejemplo, el uso del bloque de repertorio y las pruebas de HU-07.

## Workflow follow-up

- Validar el sistema con `cin324-validar-sistema` y archivar el cambio con `openspec-archive-change`.
- Actualizar `.cin324/proyecto.md` con el nombre del cambio y el estado de HU-07.
