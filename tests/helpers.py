def id_de(conexion, nombre):
    fila = conexion.execute(
        "SELECT id FROM integrantes WHERE nombre = ?", (nombre,)
    ).fetchone()
    assert fila is not None, f"No existe el integrante {nombre}"
    return fila["id"]


def id_instrumento(conexion, nombre):
    fila = conexion.execute(
        "SELECT id FROM instrumentos WHERE nombre = ?", (nombre,)
    ).fetchone()
    assert fila is not None, f"No existe el instrumento {nombre}"
    return fila["id"]


def id_cancion(conexion, titulo):
    fila = conexion.execute(
        "SELECT id FROM canciones WHERE titulo = ?", (titulo,)
    ).fetchone()
    assert fila is not None, f"No existe la canción {titulo}"
    return fila["id"]
