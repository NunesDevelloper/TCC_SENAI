from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from .auth import Rotas_Auth
from .cliente import Rotas_Cliente
from .carrinho import Rotas_Carrinho
from .combo import Rotas_Combo
from .cumpom_desconto import Rotas_CupomDesconto
from .delivre import Rotas_Delivre
from .endereco import Rotas_Endereco
from .estoque import Rotas_Estoque
from .fornecedor import Rotas_Fornecedor
from .fucionario import Rotas_Fucionario
from .historico_pedidos import Rotas_HistoricoPedidos
from .mesa import Rotas_Mesa
from .produto import Rotas_Produto
from .turno import Rotas_Turno
from ..schemas import Reposne500
from ..services import verificar_jwt_autenticado, verificar_jwt_fucionario

autenticacao_geral = [Depends(verificar_jwt_autenticado)]
autenticacao_funcionario = [Depends(verificar_jwt_fucionario)]

mr = APIRouter(
    responses={
    422:{"description":"Pasrametro do Request body invalido"},
    500:{"description":"Erro interno no servidor",
         "model":Reposne500}
    }
)

#redirecionamento para o docs altomaticamente
@mr.get("/", include_in_schema=False)
async def root_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")

#Rotas_Auth
mr.include_router(
    Rotas_Auth,
    prefix="/auth",
    tags=["auth"]
    )

#Rotas_Cliente
mr.include_router(
    Rotas_Cliente,
    prefix="/cliente",
    tags=["cliente"]
    )

#Rotas_Fucionario
mr.include_router(
    Rotas_Fucionario,
    prefix="/fucionario",
    tags=["fucionario"],
    dependencies=autenticacao_funcionario,
    )

#Rotas_Carrinho
mr.include_router(
    Rotas_Carrinho,
    prefix="/carrinho",
    tags=["carrinho"],
    )

#Rotas_Combo
mr.include_router(
    Rotas_Combo,
    prefix="/combo",
    tags=["combo"],
    dependencies=autenticacao_geral,
    )

#Rotas_CupomDesconto
mr.include_router(
    Rotas_CupomDesconto,
    prefix="/cupom_desconto",
    tags=["cupom_desconto"],
    dependencies=autenticacao_geral,
    )

#Rotas_Delivre
mr.include_router(
    Rotas_Delivre,
    prefix="/delivre",
    tags=["delivre"],
    dependencies=autenticacao_funcionario,
    )

#Rotas_Endereco
mr.include_router(
    Rotas_Endereco,
    prefix="/endereco",
    tags=["endereco"],
    )

#Rotas_Estoque
mr.include_router(
    Rotas_Estoque,
    prefix="/estoque",
    tags=["estoque"],
    dependencies=autenticacao_funcionario,
    )

#Rotas_Fornecedor
mr.include_router(
    Rotas_Fornecedor,
    prefix="/fornecedor",
    tags=["fornecedor"],
    dependencies=autenticacao_funcionario,
    )

#Rotas_HistoricoPedidos
mr.include_router(
    Rotas_HistoricoPedidos,
    prefix="/historico_pedidos",
    tags=["historico_pedidos"],
    dependencies=autenticacao_funcionario,
    )

#Rotas_Mesa
mr.include_router(
    Rotas_Mesa,
    prefix="/mesa",
    tags=["mesa"],
    dependencies=autenticacao_funcionario,
    )

#Rotas_Produto
mr.include_router(
    Rotas_Produto,
    prefix="/produto",
    tags=["produto"],
    dependencies=autenticacao_geral,
    )

#Rotas_Turno
mr.include_router(
    Rotas_Turno,
    prefix="/turno",
    tags=["turno"],
    dependencies=autenticacao_funcionario,
    )
