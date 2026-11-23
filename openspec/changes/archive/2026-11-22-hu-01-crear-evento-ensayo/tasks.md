# Tasks — HU-01 Crear evento de ensayo con roles requeridos

## 1. Estructura y dependencias

- [x] 1.1 Crear la estructura del proyecto (`app/`, `app/db/migrations/`, `app/dominio/`, `app/servicios/`, `app/integraciones/`, `app/rutas/`, `app/templates/`, `tests/`, `data/`) y verificar que existan las carpetas previstas en `design.md`.
- [x] 1.2 Crear `requirements.txt` con FastAPI, Uvicorn, Jinja2, python-multipart, pytest y httpx; verificar con `pip install -r requirements.txt` dentro del entorno virtual.

## 2. Base de datos y datos de ejemplo

- [x] 2.1 Escribir `app/db/migrations/001_esquema_inicial.sql` con las tablas `bandas`, `integrantes`, `instrumentos`, `eventos_ensayo`, `eventos_requieren_instrumentos`, `convocatorias`, `integraciones_log` y `schema_migrations`; verificar ejecutando el seed y consultando las tablas creadas.
- [x] 2.2 Implementar `app/db/conexion.py` para aplicar las migraciones en orden y registrarlas en `schema_migrations`; verificar que una segunda ejecución no reaplique migraciones.
- [x] 2.3 Implementar `app/db/seed.py` idempotente con la banda, 6 integrantes (Marta como líder, Pedro, Ana, Luis, Sofía y Diego) y el catálogo de instrumentos; verificar los conteos y que ejecutarlo dos veces no duplique datos.

## 3. Dominio y transición de estado

- [x] 3.1 Implementar `app/dominio/evento_ensayo.py` con los estados `Vigente`, `Confirmado`, `Cancelado` y `Terminado`, y la única función `transicionar(evento, evento_estado)` derivada de EST-01; verificar con una prueba unitaria que `crearEvento` lleve de Inicial a `Vigente` y que una transición no permitida falle con mensaje claro.
- [x] 3.2 Implementar `app/servicios/crear_evento.py` con las validaciones de líder, roles requeridos, quórum y fecha, la inserción del evento y la emisión de convocatorias; verificar con pruebas unitarias que cada validación impida el registro.

## 4. Integración simulada de notificaciones

- [x] 4.1 Definir la interfaz `ServicioNotificaciones` y `ServicioNotificacionesSimulado` con `enviar_convocatoria(destinatarios, evento, enlace)`, registrar la solicitud y cada entrega en `integraciones_log`, y seleccionar la implementación con `NOTIFICACIONES_MODO`; verificar con una prueba que el log contenga la solicitud y una entrega por destinatario.

## 5. Rutas y pantallas

- [x] 5.1 Crear la plantilla base con selector de usuario de demostración y `POST /demo/usuario` que guarde `usuario_id` en cookie; verificar que `GET /` liste los 6 integrantes y que el usuario elegido se conserve.
- [x] 5.2 Implementar `GET /` con la lista de eventos y enlace a «Crear evento», y `GET /eventos/nuevo` con el formulario de fecha, quórum y roles; verificar que el formulario muestre los instrumentos sembrados.
- [x] 5.3 Implementar `POST /eventos` conectando formulario, validaciones y servicio de creación; verificar que un envío válido cree el evento y redirija a su detalle.
- [x] 5.4 Implementar `GET /eventos/{id}` con fecha, quórum, roles y estado del evento; verificar que muestre el evento recién creado como `Vigente` y los mensajes de error del formulario cuando corresponda.

## 6. Pruebas de integración (escenarios Gherkin)

- [x] 6.1 Escribir la prueba «HU-01 · El líder crea un evento de ensayo y la banda es convocada» y verificar que pase con `pytest`.
- [x] 6.2 Escribir la prueba «HU-01 · Un integrante sin rol de líder intenta crear un evento de ensayo» y verificar que pase con `pytest`.
- [x] 6.3 Escribir la prueba «HU-01 · El líder intenta crear un evento de ensayo sin roles requeridos» y verificar que pase con `pytest`.
- [x] 6.4 Escribir la prueba «HU-01 · El líder intenta crear un evento de ensayo sin quórum» y verificar que pase con `pytest`.

## 7. Documentación

- [x] 7.1 Actualizar `README.md` con cómo instalar, crear la base, ejecutar y probar, y con la advertencia de que el Servicio de notificaciones está simulado; verificar ejecutando los comandos tal como quedaron escritos.

## Workflow follow-up

- Archivar el cambio con `openspec-archive-change` después de la validación del estudiante.
- Actualizar `.cin324/proyecto.md` con el nombre del cambio y los comandos de ejecución.
