-- Evaluación 2 (HU-08, HU-09): evento masivo y Representante de músicos.
-- Modelo de dominio: Integrante.rol : RolIntegrante, EventoDeEnsayo.tipo : TipoEvento,
-- EstadoEvento + Pendiente de aprobación / Rechazado, clase RevisionDeEvento.

PRAGMA foreign_keys = OFF;
BEGIN;

-- 1. Integrante.rol reemplaza al booleano es_lider (un único rol por persona).
ALTER TABLE integrantes ADD COLUMN rol TEXT NOT NULL DEFAULT 'Músico'
    CHECK (rol IN ('Músico', 'Líder de Alabanza', 'Representante de músicos'));
UPDATE integrantes SET rol = 'Líder de Alabanza' WHERE es_lider = 1;
ALTER TABLE integrantes DROP COLUMN es_lider;

-- `representa`: a lo más un Representante de músicos por banda.
CREATE UNIQUE INDEX IF NOT EXISTS ux_un_representante_por_banda
    ON integrantes (banda_id) WHERE rol = 'Representante de músicos';

-- 2. EventoDeEnsayo.tipo y los nuevos valores de EstadoEvento.
--    SQLite no permite cambiar un CHECK: se reconstruye la tabla.
CREATE TABLE eventos_ensayo_nuevo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    banda_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    quorum INTEGER NOT NULL CHECK (quorum >= 1),
    tipo TEXT NOT NULL DEFAULT 'Ensayo' CHECK (tipo IN ('Ensayo', 'Masivo')),
    estado TEXT NOT NULL DEFAULT 'Vigente'
        CHECK (estado IN ('Pendiente de aprobación', 'Vigente', 'Confirmado',
                          'Cancelado', 'Terminado', 'Rechazado')),
    CHECK (tipo = 'Masivo' OR estado NOT IN ('Pendiente de aprobación', 'Rechazado')),
    FOREIGN KEY (banda_id) REFERENCES bandas (id) ON DELETE CASCADE
);
INSERT INTO eventos_ensayo_nuevo (id, banda_id, fecha, quorum, tipo, estado)
SELECT id, banda_id, fecha, quorum, 'Ensayo', estado FROM eventos_ensayo;
DROP TABLE eventos_ensayo;
ALTER TABLE eventos_ensayo_nuevo RENAME TO eventos_ensayo;

-- 3. RevisionDeEvento (`es revisado en`: 0..1 por evento; `revisa`: el representante).
CREATE TABLE IF NOT EXISTS revisiones_evento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento_id INTEGER NOT NULL UNIQUE,
    representante_id INTEGER NOT NULL,
    decision TEXT NOT NULL CHECK (decision IN ('Aprobada', 'Rechazada')),
    justificacion TEXT,
    fecha_revision TEXT NOT NULL,
    CHECK (
        (decision = 'Rechazada' AND justificacion IS NOT NULL
            AND length(trim(justificacion)) BETWEEN 1 AND 200)
        OR (decision = 'Aprobada' AND justificacion IS NULL)
    ),
    FOREIGN KEY (evento_id) REFERENCES eventos_ensayo (id) ON DELETE CASCADE,
    FOREIGN KEY (representante_id) REFERENCES integrantes (id) ON DELETE RESTRICT
);

COMMIT;
PRAGMA foreign_keys = ON;
