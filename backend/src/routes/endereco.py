from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarEndereco, BaseEditarEndereco, ResponseDadosEndereco, ResponseOk
from ..services import alterar_dados_endereco,criar_endereco,dados_endereco,del_endereco,verificar_jwt_user

Rotas_Endereco = APIRouter(
    responses={
        404: {"description": "Não há endereço com esse id"},
        401: {"description": "Não autorizado"}
    }
)

@Rotas_Endereco.post("/criar_endereco", response_model=ResponseOk)
async def criar_Endereco(base: BaseCriarEndereco,cliente_id: int = Depends(verificar_jwt_user),session: Session = Depends(get_sesion),):
    return criar_endereco(base.logradouro, base.bairro, base.cep, cliente_id, session,base.numero, base.complemento,)


@Rotas_Endereco.get("/", response_model=ResponseDadosEndereco)
async def dados_Endereco(id: int,cliente_id: int = Depends(verificar_jwt_user),session: Session = Depends(get_sesion),):
    return dados_endereco(id, cliente_id, session)


@Rotas_Endereco.delete("/", response_model=ResponseOk)
async def deletar_Endereco(id: int,cliente_id: int = Depends(verificar_jwt_user),session: Session = Depends(get_sesion),):
    return del_endereco(id, cliente_id, session)


@Rotas_Endereco.put("/Editar_Endereco", response_model=ResponseOk)
async def editar_Endereco(base: BaseEditarEndereco,id: int,cliente_id: int = Depends(verificar_jwt_user),session: Session = Depends(get_sesion),):
    return alterar_dados_endereco(id, base.logradouro, base.bairro, base.cep, base.numero, base.complemento, cliente_id, session,)
