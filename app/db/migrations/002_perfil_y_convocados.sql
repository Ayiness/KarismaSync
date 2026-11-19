CREATE TABLE IF NOT EXISTS integrantes_instrumentos (
    integrante_id INTEGER PRIMARY KEY,
    instrumento_id INTEGER NOT NULL,
    FOREIGN KEY (integrante_id) REFERENCES integrantes (id) ON DELETE CASCADE,
    FOREIGN KEY (instrumento_id) REFERENCES instrumentos (id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS convocatorias_instrumentos (
    convocatoria_id INTEGER NOT NULL,
    instrumento_id INTEGER NOT NULL,
    PRIMARY KEY (convocatoria_id, instrumento_id),
    FOREIGN KEY (convocatoria_id) REFERENCES convocatorias (id) ON DELETE CASCADE,
    FOREIGN KEY (instrumento_id) REFERENCES instrumentos (id) ON DELETE RESTRICT
);
