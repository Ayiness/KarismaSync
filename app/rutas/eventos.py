import sqlite3
from typing import Iterator

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.db.conexion import conectar
from app.servicios.crear_evento import (
    Convocado,
    DatosNuevoEvento,
    ErrorCreacionEvento,
    crear_evento,
)
from app.servicios.registrar_asistencia import (
    ErrorRespuesta,
    EventoNoEncontrado,
    registrar_asistencia,
)
from app.vistas import templates

router = APIRouter()


def obtener_conexion() -> Iterator[sqlite3.Connection]:
    conexion = conectar()
    try:
        yield conexion
    finally:
        conexion.close()


def usuario_actual(
    request: Request, conexion: sqlite3.Connection
) -> sqlite3.Row | None:
    valor = request.cookies.get("usuario_id", "")
    if not valor.isdigit():
        return None
    return conexion.execute(
        "SELECT * FROM integrantes WHERE id = ?", (int(valor),)
    ).fetchone()


def _integrantes(conexion: sqlite3.Connection) -> list[sqlite3.Row]:
    return conexion.execute(
        "SELECT i.id, i.nombre, i.es_lider, "
        "  ii.instrumento_id AS instrumento_principal_id, "
        "  ins.nombre AS instrumento_principal "
        "FROM integrantes i "
        "LEFT JOIN integrantes_instrumentos ii ON ii.integrante_id = i.id "
        "LEFT JOIN instrumentos ins ON ins.id = ii.instrumento_id "
        "ORDER BY i.id"
    ).fetchall()


def _instrumentos(conexion: sqlite3.Connection) -> list[sqlite3.Row]:
    return conexion.execute(
        "SELECT id, nombre, es_musico_base FROM instrumentos ORDER BY id"
    ).fetchall()


def _canciones(conexion: sqlite3.Connection) -> list[sqlite3.Row]:
    return conexion.execute(
        "SELECT id, titulo, autor FROM canciones ORDER BY titulo"
    ).fetchall()


def _contexto_comun(request: Request, conexion: sqlite3.Connection) -> dict:
    return {
        "usuario": usuario_actual(request, conexion),
        "integrantes": _integrantes(conexion),
    }


def _render_formulario(
    request: Request,
    conexion: sqlite3.Connection,
    error: str | None = None,
    valores: dict | None = None,
) -> HTMLResponse:
    contexto = _contexto_comun(request, conexion)
    contexto.update(
        {
            "error": error,
            "valores": valores or {},
            "instrumentos": _instrumentos(conexion),
            "canciones": _canciones(conexion),
        }
    )
    return templates.TemplateResponse(
        request=request, name="evento_form.html", context=contexto
    )


@router.get("/", response_class=HTMLResponse)
def inicio(
    request: Request, conexion: sqlite3.Connection = Depends(obtener_conexion)
) -> HTMLResponse:
    eventos = conexion.execute(
        "SELECT e.id, e.fecha, e.quorum, e.estado, b.nombre AS banda, "
        "  (SELECT COUNT(*) FROM eventos_requieren_instrumentos r "
        "   WHERE r.evento_id = e.id) AS total_roles, "
        "  (SELECT COUNT(*) FROM convocatorias c WHERE c.evento_id = e.id) "
        "   AS total_convocatorias, "
        "  (SELECT COUNT(*) FROM eventos_canciones ec WHERE ec.evento_id = e.id) "
        "   AS total_canciones "
        "FROM eventos_ensayo e "
        "JOIN bandas b ON b.id = e.banda_id "
        "ORDER BY e.id DESC"
    ).fetchall()
    contexto = _contexto_comun(request, conexion)
    contexto["eventos"] = eventos
    return templates.TemplateResponse(request=request, name="inicio.html", context=contexto)


@router.post("/demo/usuario")
async def cambiar_usuario(
    request: Request, conexion: sqlite3.Connection = Depends(obtener_conexion)
) -> RedirectResponse:
    formulario = await request.form()
    valor = str(formulario.get("usuario_id", "")).strip()
    respuesta = RedirectResponse(url="/", status_code=303)
    if valor.isdigit() and conexion.execute(
        "SELECT 1 FROM integrantes WHERE id = ?", (int(valor),)
    ).fetchone():
        respuesta.set_cookie(
            "usuario_id", valor, httponly=True, samesite="lax", path="/"
        )
    return respuesta


@router.get("/eventos/nuevo", response_class=HTMLResponse)
def formulario_nuevo(
    request: Request, conexion: sqlite3.Connection = Depends(obtener_conexion)
) -> HTMLResponse:
    return _render_formulario(request, conexion)


@router.post("/eventos", response_class=HTMLResponse, response_model=None)
async def crear(
    request: Request, conexion: sqlite3.Connection = Depends(obtener_conexion)
) -> HTMLResponse | RedirectResponse:
    formulario = await request.form()
    fecha = str(formulario.get("fecha", "")).strip()
    quorum = str(formulario.get("quorum", "")).strip()
    convocado_ids = sorted(
        {
            int(valor)
            for valor in formulario.getlist("convocados")
            if str(valor).isdigit()
        }
    )
    instrumentos_por_integrante = {
        integrante_id: [
            int(valor)
            for valor in formulario.getlist(f"instrumentos_{integrante_id}")
            if str(valor).isdigit()
        ]
        for integrante_id in convocado_ids
    }
    convocados = [
        Convocado(
            integrante_id=integrante_id,
            instrumentos_ids=instrumentos_por_integrante[integrante_id],
        )
        for integrante_id in convocado_ids
    ]
    incluir_repertorio = formulario.get("incluir_repertorio") is not None
    canciones_ids = (
        sorted(
            {
                int(valor)
                for valor in formulario.getlist("canciones")
                if str(valor).isdigit()
            }
        )
        if incluir_repertorio
        else []
    )
    valores = {
        "fecha": fecha,
        "quorum": quorum,
        "convocados_ids": convocado_ids,
        "instrumentos_por_integrante": instrumentos_por_integrante,
        "incluir_repertorio": "1" if incluir_repertorio else "0",
        "canciones_ids": canciones_ids,
    }

    usuario = usuario_actual(request, conexion)
    if usuario is None:
        return _render_formulario(
            request,
            conexion,
            error="seleccione un usuario de demostración",
            valores=valores,
        )

    try:
        resultado = crear_evento(
            conexion,
            usuario["id"],
            DatosNuevoEvento(
                fecha=fecha,
                quorum=quorum,
                convocados=convocados,
                canciones_ids=canciones_ids,
            ),
        )
    except ErrorCreacionEvento as error:
        return _render_formulario(
            request, conexion, error=str(error), valores=valores
        )

    return RedirectResponse(url=f"/eventos/{resultado.evento_id}", status_code=303)


@router.get("/eventos/{evento_id}", response_class=HTMLResponse)
def detalle(
    evento_id: int,
    request: Request,
    conexion: sqlite3.Connection = Depends(obtener_conexion),
) -> HTMLResponse:
    return _render_detalle(request, conexion, evento_id)


@router.post(
    "/eventos/{evento_id}/asistencia", response_class=HTMLResponse, response_model=None
)
async def responder_convocatoria(
    evento_id: int,
    request: Request,
    conexion: sqlite3.Connection = Depends(obtener_conexion),
) -> HTMLResponse | RedirectResponse:
    """registrarAsistencia(evento, asiste, motivo) de DSS-05."""
    formulario = await request.form()
    respuesta = str(formulario.get("respuesta", "")).strip()
    motivo = str(formulario.get("motivo", ""))
    instrumentos_ids = [
        int(valor) for valor in formulario.getlist("instrumentos") if str(valor).isdigit()
    ]
    if respuesta not in ("confirmar", "no_asistire"):
        return _render_detalle(
            request, conexion, evento_id, error="seleccione una respuesta", motivo=motivo
        )

    usuario = usuario_actual(request, conexion)
    try:
        registrar_asistencia(
            conexion,
            usuario["id"] if usuario else None,
            evento_id,
            asiste=respuesta == "confirmar",
            motivo=motivo,
            instrumentos_ids=instrumentos_ids,
        )
    except EventoNoEncontrado as error:
        raise HTTPException(status_code=404, detail="Evento no encontrado") from error
    except ErrorRespuesta as error:
        return _render_detalle(
            request, conexion, evento_id, error=str(error), motivo=motivo
        )

    return RedirectResponse(url=f"/eventos/{evento_id}", status_code=303)


def _render_detalle(
    request: Request,
    conexion: sqlite3.Connection,
    evento_id: int,
    error: str | None = None,
    motivo: str = "",
) -> HTMLResponse:
    evento = conexion.execute(
        "SELECT e.*, b.nombre AS banda "
        "FROM eventos_ensayo e JOIN bandas b ON b.id = e.banda_id "
        "WHERE e.id = ?",
        (evento_id,),
    ).fetchone()
    if evento is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    roles = conexion.execute(
        "SELECT i.nombre FROM eventos_requieren_instrumentos r "
        "JOIN instrumentos i ON i.id = r.instrumento_id "
        "WHERE r.evento_id = ? ORDER BY i.id",
        (evento_id,),
    ).fetchall()
    # estadoConvocados(convocados[integrante, instrumentos, estadoAsistencia, motivo]) de DSS-06
    convocatorias = conexion.execute(
        "SELECT c.integrante_id, i.nombre AS integrante, c.fecha_envio, "
        "  a.estado AS estado_asistencia, a.motivo, "
        "  (SELECT GROUP_CONCAT(ins.nombre, ', ') "
        "   FROM convocatorias_instrumentos ci "
        "   JOIN instrumentos ins ON ins.id = ci.instrumento_id "
        "   WHERE ci.convocatoria_id = c.id) AS instrumentos "
        "FROM convocatorias c "
        "JOIN integrantes i ON i.id = c.integrante_id "
        "LEFT JOIN asistencias a ON a.convocatoria_id = c.id "
        "WHERE c.evento_id = ? "
        "ORDER BY i.id",
        (evento_id,),
    ).fetchall()
    canciones = conexion.execute(
        "SELECT c.titulo, c.autor FROM eventos_canciones ec "
        "JOIN canciones c ON c.id = ec.cancion_id "
        "WHERE ec.evento_id = ? ORDER BY c.titulo",
        (evento_id,),
    ).fetchall()

    usuario = usuario_actual(request, conexion)
    # detalleEvento(evento, instrumentosAsignados, estadoAsistencia) de DSS-05
    mi_convocatoria = None
    if usuario is not None:
        mi_convocatoria = next(
            (c for c in convocatorias if c["integrante_id"] == usuario["id"]), None
        )
    es_lider = usuario is not None and bool(usuario["es_lider"])
    puede_ver_respuestas = es_lider or mi_convocatoria is not None
    # El motivo de inasistencia es privado: solo lo ve el Líder de Alabanza
    # (cada integrante ve el suyo en «Tu convocatoria»). HU-03 CA9, DSS-06.
    puede_ver_motivos = es_lider

    contexto = _contexto_comun(request, conexion)
    contexto.update(
        {
            "evento": evento,
            "roles": roles,
            "convocatorias": convocatorias,
            "canciones": canciones,
            "mi_convocatoria": mi_convocatoria,
            "puede_ver_respuestas": puede_ver_respuestas,
            "puede_ver_motivos": puede_ver_motivos,
            "evento_vigente": evento["estado"] == "Vigente",
            "error": error,
            "motivo": motivo,
        }
    )
    return templates.TemplateResponse(
        request=request, name="evento_detalle.html", context=contexto
    )


def _render_perfil(
    request: Request,
    conexion: sqlite3.Connection,
    error: str | None = None,
) -> HTMLResponse:
    usuario = usuario_actual(request, conexion)
    principal = None
    if usuario is not None:
        principal = conexion.execute(
            "SELECT instrumento_id FROM integrantes_instrumentos WHERE integrante_id = ?",
            (usuario["id"],),
        ).fetchone()
    contexto = _contexto_comun(request, conexion)
    contexto.update(
        {
            "error": error,
            "instrumentos": _instrumentos(conexion),
            "instrumento_principal_id": principal["instrumento_id"] if principal else None,
        }
    )
    return templates.TemplateResponse(
        request=request, name="perfil.html", context=contexto
    )


@router.get("/perfil", response_class=HTMLResponse)
def perfil(
    request: Request, conexion: sqlite3.Connection = Depends(obtener_conexion)
) -> HTMLResponse:
    return _render_perfil(request, conexion)


@router.post("/perfil", response_class=HTMLResponse, response_model=None)
async def guardar_perfil(
    request: Request, conexion: sqlite3.Connection = Depends(obtener_conexion)
) -> HTMLResponse | RedirectResponse:
    formulario = await request.form()
    valor = str(formulario.get("instrumento_id", "")).strip()
    usuario = usuario_actual(request, conexion)
    if usuario is None:
        return _render_perfil(
            request, conexion, error="seleccione un usuario de demostración"
        )
    if not valor.isdigit() or not conexion.execute(
        "SELECT 1 FROM instrumentos WHERE id = ?", (int(valor),)
    ).fetchone():
        return _render_perfil(
            request, conexion, error="debe indicar un instrumento principal"
        )
    conexion.execute(
        "INSERT INTO integrantes_instrumentos (integrante_id, instrumento_id) "
        "VALUES (?, ?) "
        "ON CONFLICT (integrante_id) DO UPDATE SET instrumento_id = excluded.instrumento_id",
        (usuario["id"], int(valor)),
    )
    conexion.commit()
    return RedirectResponse(url="/perfil", status_code=303)
