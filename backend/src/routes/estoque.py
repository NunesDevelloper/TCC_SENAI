from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarEstoque, BaseEditarEstoque, ResponseDadosEstoque, ResponseOk
from ..services import alterar_dados_estoque, criar_estoque, dados_estoque, del_estoque

Rotas_Estoque = APIRouter(
    responses={
        404: {"description": "Não há estoque ou fornecedor com esse id"},
        409: {"description": "O ingrediente está associado a produtos ou fornecedor"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Estoque.post("/criar_estoque", response_model=ResponseOk)
async def criar_Estoque(base: BaseCriarEstoque, session: Session = Depends(get_sesion)):
    return criar_estoque(base.item_nome,base.preco_uni,base.quantidade,base.fornecedor_id,session,base.unidade_medida,)


@Rotas_Estoque.get("/", response_model=ResponseDadosEstoque)
async def dados_Estoque(id: int, session: Session = Depends(get_sesion)):
    return dados_estoque(id, session)


@Rotas_Estoque.delete("/", response_model=ResponseOk)
async def deletar_Estoque(id: int, session: Session = Depends(get_sesion)):
    return del_estoque(id, session)


@Rotas_Estoque.put("/Editar_Estoque", response_model=ResponseOk)
async def editar_Estoque(base: BaseEditarEstoque, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_estoque(
        id, base.item_nome, base.preco_uni, base.quantidade, base.unidade_medida, session
    )
