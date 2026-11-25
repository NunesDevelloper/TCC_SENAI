from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseAssociarIngredienteProduto,BaseCriarProduto,BaseEditarProduto,ResponseDadosProduto,ResponseOk
from ..services import alterar_dados_produto,associar_ingrediente_produto,criar_produto,dados_produto,del_produto,verificar_jwt_fucionario

Rotas_Produto = APIRouter(
    responses={
        404: {"description": "Não há produto com esse id"},
        409: {"description": "A operação viola a associação entre produto e ingrediente"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Produto.post("/criar_produto",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)])
async def criar_Produto(base: BaseCriarProduto, session: Session = Depends(get_sesion)):
    return criar_produto(base.categoria,base.nome,base.preco,base.desc,base.estoque_ids,session,)


@Rotas_Produto.post("/associar_ingrediente",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)])
async def associar_Ingrediente(base: BaseAssociarIngredienteProduto,session: Session = Depends(get_sesion),):
    return associar_ingrediente_produto(base.produto_id,base.estoque_id,session)


@Rotas_Produto.get("/", response_model=ResponseDadosProduto)
async def dados_Produto(id: int, session: Session = Depends(get_sesion)):
    return dados_produto(id, session)


@Rotas_Produto.delete("/",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)])
async def deletar_Produto(id: int, session: Session = Depends(get_sesion)):
    return del_produto(id, session)


@Rotas_Produto.put("/Editar_Produto",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)])
async def editar_Produto(base: BaseEditarProduto, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_produto(id, base.categoria, base.nome, base.preco, base.desc, session)
