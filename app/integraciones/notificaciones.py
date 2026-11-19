import json
import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Mapping, Protocol, Sequence


@dataclass
class RespuestaEnvio:
    aceptada: bool
    mensaje: str


class ServicioNotificaciones(Protocol):
    def enviar_convocatoria(
        self,
        destinatarios: Sequence[sqlite3.Row],
        evento: Mapping[str, object],
        enlace: str,
    ) -> RespuestaEnvio: ...


class ServicioNotificacionesSimulado:
    def __init__(self, conexion: sqlite3.Connection) -> None:
        self.conexion = conexion

    def _registrar(self, mensaje: str, detalle: dict) -> None:
        self.conexion.execute(
            "INSERT INTO integraciones_log (sistema, mensaje, detalle, fecha) "
            "VALUES (?, ?, ?, ?)",
            (
                "Servicio de notificaciones",
                mensaje,
                json.dumps(detalle, ensure_ascii=False),
                datetime.now(timezone.utc).isoformat(timespec="seconds"),
            ),
        )

    def enviar_convocatoria(
        self,
        destinatarios: Sequence[sqlite3.Row],
        evento: Mapping[str, object],
        enlace: str,
    ) -> RespuestaEnvio:
        ids = [fila["id"] for fila in destinatarios]
        self._registrar(
            "enviarConvocatoria",
            {"destinatarios": ids, "evento": dict(evento), "enlace": enlace},
        )
        for fila in destinatarios:
            self._registrar(
                "entrega convocatoria",
                {
                    "integrante_id": fila["id"],
                    "integrante": fila["nombre"],
                    "evento": dict(evento),
                    "enlace": enlace,
                },
            )
        return RespuestaEnvio(aceptada=True, mensaje="solicitudAceptada")


def obtener_servicio_notificaciones(
    conexion: sqlite3.Connection,
) -> ServicioNotificaciones:
    modo = os.environ.get("NOTIFICACIONES_MODO", "simulado").strip().lower()
    if modo != "simulado":
        raise ValueError(f"Modo de notificaciones no soportado: {modo}")
    return ServicioNotificacionesSimulado(conexion)
