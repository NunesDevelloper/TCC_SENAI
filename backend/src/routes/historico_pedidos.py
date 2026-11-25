from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarHistoricoPedidos, BaseEditarHistoricoPedidos, ResponseDadosHistoricoPedidos, ResponseOk
from ..services import (
    alterar_dados_historico_pedidos,
    criar_historico_pedidos,
    dados_historico_pedidos,
    del_historico_pedidos,
)

Rotas_HistoricoPedidos = APIRouter(
    responses={
        404: {"description": "Não há histórico de pedidos com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_HistoricoPedidos.post("/criar_historico_pedidos", response_model=ResponseOk)
async def criar_HistoricoPedidos(base: BaseCriarHistoricoPedidos, session: Session = Depends(get_sesion)):
    return criar_historico_pedidos(base.carrinho_id, session, base.status)


@Rotas_HistoricoPedidos.get("/", response_model=ResponseDadosHistoricoPedidos)
async def dados_HistoricoPedidos(id: int, session: Session = Depends(get_sesion)):
    return dados_historico_pedidos(id, session)


@Rotas_HistoricoPedidos.delete("/", response_model=ResponseOk)
async def deletar_HistoricoPedidos(id: int, session: Session = Depends(get_sesion)):
    return del_historico_pedidos(id, session)


@Rotas_HistoricoPedidos.put("/Editar_HistoricoPedidos", response_model=ResponseOk)
async def editar_HistoricoPedidos(base: BaseEditarHistoricoPedidos, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_historico_pedidos(id, base.carrinho_id, base.status, session)
