# Proposal — HU-06 Registrar el perfil instrumental del integrante

> Nota: este cambio documenta en OpenSpec una historia que ya se había generado el 2026-11-05 junto con HU-01 (migración `002_perfil_y_convocados.sql`) sin un cambio propio. Se registra para que cada HU tenga su cambio trazable, tal como pide la Entrega de proyecto 3.

## Why

Para convocar a un ensayo, el Líder de Alabanza necesita saber con qué instrumento toca cada integrante. Hoy ese dato se pregunta por mensaje en cada convocatoria. HU-06 permite que cada integrante registre su instrumento principal una sola vez, y que ese instrumento aparezca preseleccionado al crear un evento (HU-01).

## What Changes

- Nueva pantalla «Perfil» (`GET /perfil`) donde el integrante identificado elige su instrumento principal del catálogo.
- `POST /perfil` registra el instrumento principal o lo reemplaza si ya existía.
- Si no se indica instrumento, el perfil no se registra y se informa el error.
- El formulario de creación de eventos muestra el instrumento principal de cada integrante.
- El seed asigna un instrumento principal de ejemplo a cada integrante.

## Capabilities

### New Capabilities
- `perfil-instrumental`: registro y cambio del instrumento principal del integrante.

### Modified Capabilities
- `eventos-ensayo`: el formulario de creación muestra y preselecciona el instrumento principal de cada convocado.

## Impact

- Código: migración `002_perfil_y_convocados.sql` (tabla `integrantes_instrumentos`), `app/rutas/eventos.py` (`perfil`, `guardar_perfil`), plantilla `perfil.html`, `app/db/seed.py`.
- Pruebas: `tests/test_hu06_perfil_instrumental.py`, una prueba por escenario Gherkin.
- Fuera de alcance: varios instrumentos principales, nivel de habilidad, autenticación real.
- Trazabilidad: HU-06, RF-12, CU-03, DSS-03. No afecta EST-01 ni EST-02.
