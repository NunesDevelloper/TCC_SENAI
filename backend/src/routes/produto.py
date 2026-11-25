from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarProduto, BaseEditarProduto, ResponseDadosProduto, ResponseOk
from ..services import alterar_dados_produto, criar_produto, dados_produto, del_produto

Rotas_Produto = APIRouter(
    responses={
        404: {"description": "Não há produto com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Produto.post("/criar_produto", response_model=ResponseOk)
async def criar_Produto(base: BaseCriarProduto, session: Session = Depends(get_sesion)):
    return criar_produto(base.categoria, base.nome, base.preco, base.desc, session)


@Rotas_Produto.get("/", response_model=ResponseDadosProduto)
async def dados_Produto(id: int, session: Session = Depends(get_sesion)):
    return dados_produto(id, session)


@Rotas_Produto.delete("/", response_model=ResponseOk)
async def deletar_Produto(id: int, session: Session = Depends(get_sesion)):
    return del_produto(id, session)


@Rotas_Produto.put("/Editar_Produto", response_model=ResponseOk)
async def editar_Produto(base: BaseEditarProduto, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_produto(id, base.categoria, base.nome, base.preco, base.desc, session)
