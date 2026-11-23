# Design — HU-06 Registrar el perfil instrumental del integrante

## Context

Fuentes: `04-historias-usuario.md` (HU-06), `07-criterios-aceptacion.md` (HU-06), `08-modelo-dominio.md` (asociación entre `Integrante` e `Instrumento` como instrumento principal), `09-casos-uso.md` (CU-03) y `10-diagramas-secuencia.md` (DSS-03). El instrumento principal es un dato del integrante y no cambia el ciclo de vida del evento ni de la asistencia.

## Goals / Non-Goals

**Goals:**
- Registrar un único instrumento principal por integrante.
- Permitir cambiarlo.
- Rechazar el guardado sin instrumento.
- Mostrarlo al Líder al crear un evento.

**Non-Goals:**
- Varios instrumentos principales o secundarios en el perfil.
- Autenticación real (se usa el selector de usuario de demostración).

## Decisions

### Modelo de datos

| Tabla | Columnas | Origen y reglas |
|-------|----------|-----------------|
| `integrantes_instrumentos` | `integrante_id PK`, `instrumento_id` | Instrumento principal: multiplicidad 0..1 desde `Integrante`, por eso `integrante_id` es clave primaria. `ON DELETE CASCADE` desde el integrante y `ON DELETE RESTRICT` desde el instrumento. |

### Rutas (derivadas de CU-03 y DSS-03)

| Método y ruta | Mensaje de DSS-03 | Resultado |
|---------------|-------------------|-----------|
| `GET /perfil` | `abrirPerfil()` / `formularioPerfil(...)` | Catálogo de instrumentos con el actual seleccionado. |
| `POST /perfil` | `guardarPerfil(instrumentoPrincipal)` | Inserta o reemplaza (`ON CONFLICT ... DO UPDATE`) y redirige a `/perfil`. |
| `POST /perfil` sin instrumento | `error(...)` | Responde 200 con «debe indicar un instrumento principal»; no guarda. |

### Validaciones

- El instrumento debe existir en el catálogo.
- Sin usuario de demostración seleccionado no se guarda nada.

## Risks / Trade-offs

- [Sin autenticación real] → cualquiera puede elegir usuario en la demo; aceptable para el alcance del curso.
