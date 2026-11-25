from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarCarrinho, BaseEditarCarrinho, ResponseDadosCarrinho, ResponseOk
from ..services import alterar_dados_carrinho, criar_carrinho, dados_carrinho, del_carrinho

Rotas_Carrinho = APIRouter(
    responses={
        404: {"description": "Não há carrinho com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Carrinho.post("/criar_carrinho", response_model=ResponseOk)
async def criar_Carrinho(base: BaseCriarCarrinho, session: Session = Depends(get_sesion)):
    return criar_carrinho(
        base.cliente_id, base.funcionario_id, base.mesa_id, base.cupom_desconto_id,
        session, base.is_delivre, base.is_retirada, base.metedo_pagamento
    )


@Rotas_Carrinho.get("/", response_model=ResponseDadosCarrinho)
async def dados_Carrinho(id: int, session: Session = Depends(get_sesion)):
    return dados_carrinho(id, session)


@Rotas_Carrinho.delete("/", response_model=ResponseOk)
async def deletar_Carrinho(id: int, session: Session = Depends(get_sesion)):
    return del_carrinho(id, session)


@Rotas_Carrinho.put("/Editar_Carrinho", response_model=ResponseOk)
async def editar_Carrinho(base: BaseEditarCarrinho, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_carrinho(
        id, session, base.cliente_id, base.funcionario_id, base.mesa_id,
        base.cupom_desconto_id, base.is_delivre, base.is_retirada, base.metedo_pagamento
    )
