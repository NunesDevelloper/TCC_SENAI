from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarCombo, BaseEditarCombo, ResponseDadosCombo, ResponseOk
from ..services import alterar_dados_combo,criar_combo,dados_combo,del_combo,verificar_jwt_fucionario


Rotas_Combo = APIRouter(
    responses={
        404: {"description": "Não há combo com esse id"},
        409: {"description": "O preço do combo não pode ser negativo"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Combo.post("/criar_combo",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)],)
async def criar_Combo(base: BaseCriarCombo, session: Session = Depends(get_sesion)):
    return criar_combo(base.nome, base.preco, session, base.desc)


@Rotas_Combo.get("/", response_model=ResponseDadosCombo)
async def dados_Combo(id: int, session: Session = Depends(get_sesion)):
    return dados_combo(id, session)


@Rotas_Combo.delete( "/", response_model=ResponseOk, dependencies=[Depends(verificar_jwt_fucionario)],)
async def deletar_Combo(id: int, session: Session = Depends(get_sesion)):
    return del_combo(id, session)


@Rotas_Combo.put("/Editar_Combo",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)])
async def editar_Combo(base: BaseEditarCombo, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_combo(id, base.nome, base.preco, base.desc, session)
