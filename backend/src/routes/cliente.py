from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import ResponseOk, BaseEditarCliente, ResponseDadosCliente, BaseCriarCliente
from ..services import alterar_dados_cliente, criar_conta_cliente, dados_cliente, del_acont_cliente

Rotas_Cliente = APIRouter(
    responses={
        404: {
            "description":"Não há User Verificado com esse Email/Senha Invalida"
        },
        401:{
            "description":"Não Altorizado"
        }
    }
)

#Depends(verificar_jwt_user)

@Rotas_Cliente.post("/criar_user",response_model=ResponseOk)
async def Editar_User(base : BaseCriarCliente, session: Session = Depends(get_sesion)):
    return criar_conta_cliente(base.nome, base.senha, base.email, session)

@Rotas_Cliente.get("/", response_model=ResponseDadosCliente)
async def dados_User(id: int , session: Session = Depends(get_sesion)):
    """\n Pega os dados do User"""
    return dados_cliente(id, session)

@Rotas_Cliente.delete("/", response_model=ResponseOk)
async def Dell_User(id: int, session: Session = Depends(get_sesion)):
    """\n Deletar o User"""
    return del_acont_cliente(id, session)

@Rotas_Cliente.put("/Editar_User",response_model=ResponseOk)
async def Editar_User(base : BaseEditarCliente, id: int, session: Session = Depends(get_sesion)):
    """\n Alterar dados do user \n \n \
        nome | senha é opicional \
        OS DOIS PAREMETROS NÃO PODE SER Null\n \n \
    """

    return alterar_dados_cliente(id, base.nome, base.senha, session)

