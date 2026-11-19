CREATE TABLE IF NOT EXISTS canciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    autor TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS eventos_canciones (
    evento_id INTEGER NOT NULL,
    cancion_id INTEGER NOT NULL,
    PRIMARY KEY (evento_id, cancion_id),
    FOREIGN KEY (evento_id) REFERENCES eventos_ensayo (id) ON DELETE CASCADE,
    FOREIGN KEY (cancion_id) REFERENCES canciones (id) ON DELETE RESTRICT
);
