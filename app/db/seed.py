import sqlite3

from app.db.conexion import conectar

NOMBRE_BANDA = "KarismaSync"
INTEGRANTES = [
    ("Marta", 1),
    ("Pedro", 0),
    ("Ana", 0),
    ("Luis", 0),
    ("Sofía", 0),
    ("Diego", 0),
]
INSTRUMENTOS = [
    ("batería", 1),
    ("bajo", 1),
    ("guitarra eléctrica", 1),
    ("guitarra acústica", 1),
    ("teclado", 1),
    ("voz", 0),
]
PERFILES = {
    "Marta": "voz",
    "Pedro": "guitarra eléctrica",
    "Ana": "teclado",
    "Luis": "batería",
    "Sofía": "bajo",
    "Diego": "guitarra acústica",
}
CANCIONES = [
    ("Cuán grande es Él", "Stuart K. Hine"),
    ("Sublime gracia", "John Newton"),
    ("Santo, santo, santo", "Reginald Heber"),
    ("Alabaré", "Manuel José Alonso"),
    ("Te alabaré mi buen Jesús", "Marcos Witt"),
    ("Renuévame", "Marcos Witt"),
    ("Tu fidelidad", "Marcos Witt"),
    ("Grande es tu amor", "Chris Tomlin"),
    ("Dios está aquí", "Tradicional"),
    ("Levanto mis manos", "Marcos Witt"),
    ("Abre mis ojos", "Jesús Adrián Romero"),
    ("Eres mi todo", "Jesús Adrián Romero"),
    ("Mi esperanza está en Jesús", "Marcos Witt"),
    ("Cristo vive", "Tradicional"),
    ("Digno eres", "Tradicional"),
    ("Nadie como tú", "Tradicional"),
    ("Tu gracia es suficiente", "Tradicional"),
    ("Cantamos aleluya", "Tradicional"),
    ("El amor de Dios", "Tradicional"),
    ("Eres digno", "Tradicional"),
]


def sembrar(conexion: sqlite3.Connection) -> None:
    with conexion:
        conexion.execute("INSERT OR IGNORE INTO bandas (nombre) VALUES (?)", (NOMBRE_BANDA,))
        banda = conexion.execute(
            "SELECT id FROM bandas WHERE nombre = ?", (NOMBRE_BANDA,)
        ).fetchone()
        for nombre, es_lider in INTEGRANTES:
            conexion.execute(
                "INSERT OR IGNORE INTO integrantes (nombre, banda_id, es_lider) VALUES (?, ?, ?)",
                (nombre, banda["id"], es_lider),
            )
        for nombre, es_musico_base in INSTRUMENTOS:
            conexion.execute(
                "INSERT OR IGNORE INTO instrumentos (nombre, es_musico_base) VALUES (?, ?)",
                (nombre, es_musico_base),
            )
        for titulo, autor in CANCIONES:
            conexion.execute(
                "INSERT OR IGNORE INTO canciones (titulo, autor) VALUES (?, ?)",
                (titulo, autor),
            )

        guitarra = conexion.execute(
            "SELECT id FROM instrumentos WHERE nombre = 'guitarra'"
        ).fetchone()
        electrica = conexion.execute(
            "SELECT id FROM instrumentos WHERE nombre = 'guitarra eléctrica'"
        ).fetchone()
        if guitarra is not None and electrica is not None:
            for tabla, columna in [
                ("eventos_requieren_instrumentos", "evento_id"),
                ("integrantes_instrumentos", "integrante_id"),
                ("convocatorias_instrumentos", "convocatoria_id"),
            ]:
                conexion.execute(
                    f"INSERT OR IGNORE INTO {tabla} ({columna}, instrumento_id) "
                    f"SELECT {columna}, ? FROM {tabla} WHERE instrumento_id = ?",
                    (electrica["id"], guitarra["id"]),
                )
                conexion.execute(
                    f"DELETE FROM {tabla} WHERE instrumento_id = ?", (guitarra["id"],)
                )
            conexion.execute("DELETE FROM instrumentos WHERE id = ?", (guitarra["id"],))

        for nombre_integrante, nombre_instrumento in PERFILES.items():
            integrante = conexion.execute(
                "SELECT id FROM integrantes WHERE nombre = ? AND banda_id = ?",
                (nombre_integrante, banda["id"]),
            ).fetchone()
            instrumento = conexion.execute(
                "SELECT id FROM instrumentos WHERE nombre = ?", (nombre_instrumento,)
            ).fetchone()
            if integrante is None or instrumento is None:
                continue
            conexion.execute(
                "INSERT OR IGNORE INTO integrantes_instrumentos (integrante_id, instrumento_id) "
                "VALUES (?, ?)",
                (integrante["id"], instrumento["id"]),
            )


def main() -> None:
    conexion = conectar()
    try:
        sembrar(conexion)
        total_integrantes = conexion.execute("SELECT COUNT(*) FROM integrantes").fetchone()[0]
        total_instrumentos = conexion.execute("SELECT COUNT(*) FROM instrumentos").fetchone()[0]
        total_canciones = conexion.execute("SELECT COUNT(*) FROM canciones").fetchone()[0]
        print(
            f"Datos de ejemplo listos: {total_integrantes} integrantes, "
            f"{total_instrumentos} instrumentos, {total_canciones} canciones."
        )
    finally:
        conexion.close()


if __name__ == "__main__":
    main()
