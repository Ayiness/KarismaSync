"""Roles del Integrante (modelo de dominio: RolIntegrante, `lidera`, `representa`)."""

from enum import Enum


class RolIntegrante(str, Enum):
    MUSICO = "Músico"
    LIDER = "Líder de Alabanza"
    REPRESENTANTE = "Representante de músicos"


def es_lider(integrante) -> bool:
    return integrante is not None and integrante["rol"] == RolIntegrante.LIDER.value


def es_representante(integrante) -> bool:
    return (
        integrante is not None
        and integrante["rol"] == RolIntegrante.REPRESENTANTE.value
    )
