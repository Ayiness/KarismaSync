from fastapi import FastAPI

from app.rutas.eventos import router

app = FastAPI(
    title="KarismaSync",
    description="Gestión de convocatorias y ensayos de la banda.",
)
app.include_router(router)
