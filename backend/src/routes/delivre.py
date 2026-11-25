from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseAssociarPedidoDelivre,BaseCriarDelivre,BaseEditarDelivre,ResponseDadosDelivre,ResponseOk
from ..services import alterar_dados_delivre,associar_pedido_delivre,criar_delivre,dados_delivre,del_delivre,listar_delivres,verificar_jwt_fucionario


Rotas_Delivre = APIRouter(
    responses={
        404: {"description": "Não há delivre com esse id"},
        409: {"description": "A atribuição de entregador viola as regras do pedido"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Delivre.post("/criar_delivre", response_model=ResponseOk)
async def criar_Delivre(base: BaseCriarDelivre, session: Session = Depends(get_sesion)):
    return criar_delivre(base.nome, session)


@Rotas_Delivre.post("/associar_pedido", response_model=ResponseOk)
async def associar_Pedido(base: BaseAssociarPedidoDelivre,session: Session = Depends(get_sesion)):
    return associar_pedido_delivre(base.delivre_id, base.carrinho_id, session)


@Rotas_Delivre.get("/", response_model=ResponseDadosDelivre)
async def dados_Delivre(id: int, session: Session = Depends(get_sesion)):
    return dados_delivre(id, session)


@Rotas_Delivre.get("/todos", dependencies=[Depends(verificar_jwt_fucionario)])
async def todos_Delivres(session: Session = Depends(get_sesion)):
    return listar_delivres(session)


@Rotas_Delivre.delete("/", response_model=ResponseOk)
async def deletar_Delivre(id: int, session: Session = Depends(get_sesion)):
    return del_delivre(id, session)


@Rotas_Delivre.put("/Editar_Delivre", response_model=ResponseOk)
async def editar_Delivre(base: BaseEditarDelivre, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_delivre(id, base.nome, session)
