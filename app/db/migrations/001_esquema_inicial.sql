CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS integrantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    banda_id INTEGER NOT NULL,
    es_lider INTEGER NOT NULL DEFAULT 0 CHECK (es_lider IN (0, 1)),
    UNIQUE (banda_id, nombre),
    FOREIGN KEY (banda_id) REFERENCES bandas (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS instrumentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    es_musico_base INTEGER NOT NULL DEFAULT 0 CHECK (es_musico_base IN (0, 1))
);

CREATE TABLE IF NOT EXISTS eventos_ensayo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    banda_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    quorum INTEGER NOT NULL CHECK (quorum >= 1),
    estado TEXT NOT NULL DEFAULT 'Vigente'
        CHECK (estado IN ('Vigente', 'Confirmado', 'Cancelado', 'Terminado')),
    FOREIGN KEY (banda_id) REFERENCES bandas (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS eventos_requieren_instrumentos (
    evento_id INTEGER NOT NULL,
    instrumento_id INTEGER NOT NULL,
    PRIMARY KEY (evento_id, instrumento_id),
    FOREIGN KEY (evento_id) REFERENCES eventos_ensayo (id) ON DELETE CASCADE,
    FOREIGN KEY (instrumento_id) REFERENCES instrumentos (id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS convocatorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento_id INTEGER NOT NULL,
    integrante_id INTEGER NOT NULL,
    fecha_ensayo TEXT NOT NULL,
    fecha_envio TEXT NOT NULL,
    UNIQUE (evento_id, integrante_id),
    FOREIGN KEY (evento_id) REFERENCES eventos_ensayo (id) ON DELETE CASCADE,
    FOREIGN KEY (integrante_id) REFERENCES integrantes (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS integraciones_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sistema TEXT NOT NULL,
    mensaje TEXT NOT NULL,
    detalle TEXT NOT NULL,
    fecha TEXT NOT NULL
);
