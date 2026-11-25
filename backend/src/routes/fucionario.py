from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarFucionario, BaseEditarFucionario, ResponseDadosFucionario, ResponseOk
from ..services import alterar_dados_fucionario, criar_conta_fucionario, dados_fucionario, del_acont_fucionario

Rotas_Fucionario = APIRouter(
    responses={
        404: {"description": "Não há funcionário com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Fucionario.post("/criar_fucionario", response_model=ResponseOk)
async def criar_Fucionario(base: BaseCriarFucionario, session: Session = Depends(get_sesion)):
    return criar_conta_fucionario(base.nome, base.senha, base.login, session)


@Rotas_Fucionario.get("/", response_model=ResponseDadosFucionario)
async def dados_Fucionario(id: int, session: Session = Depends(get_sesion)):
    return dados_fucionario(id, session)


@Rotas_Fucionario.delete("/", response_model=ResponseOk)
async def deletar_Fucionario(id: int, session: Session = Depends(get_sesion)):
    return del_acont_fucionario(id, session)


@Rotas_Fucionario.put("/Editar_Fucionario", response_model=ResponseOk)
async def editar_Fucionario(base: BaseEditarFucionario, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_fucionario(id, base.senha, base.nome, session)
