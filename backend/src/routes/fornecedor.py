from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseAssociarFornecedorEstoque,BaseCriarFornecedor,BaseEditarFornecedor,ResponseDadosFornecedor,ResponseOk
from ..services import alterar_dados_fornecedor,associar_fornecedor_estoque,criar_fornecedor,dados_fornecedor,del_fornecedor,listar_fornecedores,verificar_jwt_fucionario

Rotas_Fornecedor = APIRouter(
    responses={
        404: {"description": "Não há fornecedor com esse id"},
        409: {"description": "A operação viola a associação entre fornecedor e ingrediente"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Fornecedor.post("/criar_fornecedor", response_model=ResponseOk)
async def criar_Fornecedor(base: BaseCriarFornecedor, session: Session = Depends(get_sesion)):
    return criar_fornecedor(base.cnpj, base.nome, base.contato, session)


@Rotas_Fornecedor.post("/associar_estoque", response_model=ResponseOk)
async def associar_Estoque(base: BaseAssociarFornecedorEstoque,session: Session = Depends(get_sesion)):
    return associar_fornecedor_estoque(base.fornecedor_id,base.estoque_id,session,)


@Rotas_Fornecedor.get("/", response_model=ResponseDadosFornecedor)
async def dados_Fornecedor(id: int, session: Session = Depends(get_sesion)):
    return dados_fornecedor(id, session)


@Rotas_Fornecedor.get("/todos", dependencies=[Depends(verificar_jwt_fucionario)])
async def todos_Fornecedores(session: Session = Depends(get_sesion)):
    return listar_fornecedores(session)


@Rotas_Fornecedor.delete("/", response_model=ResponseOk)
async def deletar_Fornecedor(id: int, session: Session = Depends(get_sesion)):
    return del_fornecedor(id, session)


@Rotas_Fornecedor.put("/Editar_Fornecedor", response_model=ResponseOk)
async def editar_Fornecedor(base: BaseEditarFornecedor, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_fornecedor(id, base.cnpj, base.nome, base.contato, session)
