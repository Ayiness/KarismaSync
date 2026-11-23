# Design — HU-01 Quórum obligatorio y sincronización de la spec

## Context

Fuentes: HU-01 en `04-historias-usuario.md` (CA4) y `07-criterios-aceptacion.md`, CU-01 en `09-casos-uso.md` y DSS-01. El quórum es el atributo `quorum` de `EventoDeEnsayo` en `08-modelo-dominio.md`; la tabla `eventos_ensayo` ya lo exige `NOT NULL` y `>= 1`.

## Decisions

### Validación del quórum (en `crear_evento`)

Se valida después de los convocados y sus instrumentos, y antes de la fecha:

| Entrada | Resultado |
|---------|-----------|
| vacío, no numérico o menor que 1 | `ErrorCreacionEvento("debe indicar el quórum requerido")` |
| mayor que la cantidad de convocados | `ErrorCreacionEvento("el quórum no puede superar la cantidad de músicos convocados")` |
| entre 1 y la cantidad de convocados | se registra el evento |

En los dos casos de error no se inserta nada ni se envían convocatorias, y la ruta `POST /eventos` vuelve al formulario con el mensaje (rama `creacionRechazada(motivo: datosInvalidos)` de DSS-01).

### Formulario

El campo `quorum` se muestra vacío; si el formulario vuelve con un error, conserva el valor que escribió el líder. Mantiene `required` y `min="1"` como ayuda del navegador; la regla se garantiza en el servidor.

### Decisión del equipo

2026-11-23 — Confirmado por el estudiante: el campo aparece vacío (no se propone la cantidad de convocados) y un quórum mayor que los convocados se rechaza.

## Risks / Trade-offs

- [El líder debe escribir el quórum en cada evento] → Es intencional: el quórum es una decisión explícita del líder.
