from ..db import Base, engine
from .muitas_muitas import carrinho_produto, cliente_endereco, delivre_carrinho, estoque_fornecidor, estoque_produto
from .carrinho import EnumMetedoPagamento, Carrinho
from .cliente import Cliente
from .combo import Combo
from .cumpom_desconto import CupomDesconto
from .delivre import Delivre
from .endereco import Endereco
from .estoque import EnumUnidadeMedida, Estoque
from .fornecedor import Fornecedor
from .fucionario import Funcionario
from .historico_pedidos import HistoricoPedidos
from .mesa import Mesa
from .produto import EnumCategoria, Produto

__all__ = [
    "carrinho_produto","cliente_endereco","delivre_carrinho","estoque_fornecidor","estoque_produto","EnumMetedoPagamento","Carrinho","Cliente","Combo",
    "CupomDesconto","Delivre","Endereco","EnumUnidadeMedida","Estoque","Fornecedor","Funcionario","HistoricoPedidos","Mesa","EnumCategoria","Produto",
]

Base.metadata.create_all(bind=engine)