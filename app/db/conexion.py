import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
MIGRATIONS_DIR = Path(__file__).resolve().parent / "migrations"


def ruta_base_datos() -> Path:
    return Path(os.environ.get("KARISMASYNC_DB", BASE_DIR / "data" / "app.db"))


def aplicar_migraciones(conexion: sqlite3.Connection) -> None:
    conexion.execute(
        "CREATE TABLE IF NOT EXISTS schema_migrations ("
        "version TEXT PRIMARY KEY, applied_at TEXT NOT NULL)"
    )
    aplicadas = {
        fila["version"] for fila in conexion.execute("SELECT version FROM schema_migrations")
    }
    for archivo in sorted(MIGRATIONS_DIR.glob("*.sql")):
        version = archivo.stem
        if version in aplicadas:
            continue
        conexion.executescript(archivo.read_text(encoding="utf-8"))
        conexion.execute(
            "INSERT INTO schema_migrations (version, applied_at) VALUES (?, ?)",
            (version, datetime.now(timezone.utc).isoformat(timespec="seconds")),
        )
        conexion.commit()


def conectar(ruta: str | Path | None = None) -> sqlite3.Connection:
    destino = Path(ruta) if ruta is not None else ruta_base_datos()
    destino.parent.mkdir(parents=True, exist_ok=True)
    conexion = sqlite3.connect(destino, check_same_thread=False)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    aplicar_migraciones(conexion)
    return conexion
