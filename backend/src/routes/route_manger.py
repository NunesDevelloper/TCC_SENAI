from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from .cliente import Rotas_Cliente
from ..schemas import Reposne500

mr = APIRouter(
    responses={
    422:{"description":"Pasrametro do Request body invalido"},
    500:{"description":"Erro interno no servidor",
         "model":Reposne500}
    }
)

@mr.get("/", include_in_schema=False)
async def root_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")

 
mr.include_router(
    Rotas_Cliente,
    prefix="/cliente",
    tags=["cliente"]
    )