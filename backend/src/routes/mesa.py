from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarMesa, BaseEditarMesa, ResponseDadosMesa, ResponseOk
from ..services import alterar_dados_mesa, criar_mesa, dados_mesa, del_mesa

Rotas_Mesa = APIRouter(
    responses={
        404: {"description": "Não há mesa com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Mesa.post("/criar_mesa", response_model=ResponseOk)
async def criar_Mesa(base: BaseCriarMesa, session: Session = Depends(get_sesion)):
    return criar_mesa(base.numero, session)


@Rotas_Mesa.get("/", response_model=ResponseDadosMesa)
async def dados_Mesa(id: int, session: Session = Depends(get_sesion)):
    return dados_mesa(id, session)


@Rotas_Mesa.delete("/", response_model=ResponseOk)
async def deletar_Mesa(id: int, session: Session = Depends(get_sesion)):
    return del_mesa(id, session)


@Rotas_Mesa.put("/Editar_Mesa", response_model=ResponseOk)
async def editar_Mesa(base: BaseEditarMesa, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_mesa(id, base.numero, session)
