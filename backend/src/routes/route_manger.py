from fastapi import APIRouter
from fastapi.responses import RedirectResponse
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
    tags=["fucionario"]
    )

#Rotas_Carrinho
mr.include_router(
    Rotas_Carrinho,
    prefix="/carrinho",
    tags=["carrinho"]
    )

#Rotas_Combo
mr.include_router(
    Rotas_Combo,
    prefix="/combo",
    tags=["combo"]
    )

#Rotas_CupomDesconto
mr.include_router(
    Rotas_CupomDesconto,
    prefix="/cupom_desconto",
    tags=["cupom_desconto"]
    )

#Rotas_Delivre
mr.include_router(
    Rotas_Delivre,
    prefix="/delivre",
    tags=["delivre"]
    )

#Rotas_Endereco
mr.include_router(
    Rotas_Endereco,
    prefix="/endereco",
    tags=["endereco"]
    )

#Rotas_Estoque
mr.include_router(
    Rotas_Estoque,
    prefix="/estoque",
    tags=["estoque"]
    )

#Rotas_Fornecedor
mr.include_router(
    Rotas_Fornecedor,
    prefix="/fornecedor",
    tags=["fornecedor"]
    )

#Rotas_HistoricoPedidos
mr.include_router(
    Rotas_HistoricoPedidos,
    prefix="/historico_pedidos",
    tags=["historico_pedidos"]
    )

#Rotas_Mesa
mr.include_router(
    Rotas_Mesa,
    prefix="/mesa",
    tags=["mesa"]
    )

#Rotas_Produto
mr.include_router(
    Rotas_Produto,
    prefix="/produto",
    tags=["produto"]
    )

#Rotas_Turno
mr.include_router(
    Rotas_Turno,
    prefix="/turno",
    tags=["turno"]
    )
