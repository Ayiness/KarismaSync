import pytest
from fastapi.testclient import TestClient

from app.db.conexion import conectar
from app.db.seed import sembrar


@pytest.fixture
def conexion(tmp_path, monkeypatch):
    ruta = tmp_path / "karismasync_test.db"
    monkeypatch.setenv("KARISMASYNC_DB", str(ruta))
    conexion = conectar()
    sembrar(conexion)
    yield conexion
    conexion.close()


@pytest.fixture
def cliente(conexion):
    from app.main import app

    return TestClient(app)
