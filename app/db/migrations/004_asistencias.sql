-- HU-03: Asistencia de cada convocatoria (clase Asistencia, asociación `tiene`, EST-02).
CREATE TABLE IF NOT EXISTS asistencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    convocatoria_id INTEGER NOT NULL UNIQUE,
    estado TEXT NOT NULL DEFAULT 'Pendiente'
        CHECK (estado IN ('Pendiente', 'Confirmada', 'No asiste', 'Sin respuesta')),
    motivo TEXT,
    fecha_respuesta TEXT,
    CHECK (
        (estado = 'No asiste' AND motivo IS NOT NULL
            AND length(trim(motivo)) BETWEEN 1 AND 200)
        OR (estado <> 'No asiste' AND motivo IS NULL)
    ),
    FOREIGN KEY (convocatoria_id) REFERENCES convocatorias (id) ON DELETE CASCADE
);

-- Las convocatorias emitidas antes de HU-03 nacen con su asistencia Pendiente
-- (transición convocatoriaEmitida de EST-02).
INSERT INTO asistencias (convocatoria_id, estado)
SELECT c.id, 'Pendiente'
FROM convocatorias c
WHERE NOT EXISTS (SELECT 1 FROM asistencias a WHERE a.convocatoria_id = c.id);
