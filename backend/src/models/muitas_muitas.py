from sqlalchemy import Table, Column, Integer, ForeignKey
from ..db import Base

#Tabela de associação entre Estoque e Fornecedor
estoque_fornecidor = Table(
    'estoque_fornecidor', Base.metadata,
    Column('estoque_id', Integer, ForeignKey('estoque.id'), primary_key=True),
    Column('fornecidor_id', Integer, ForeignKey('fornecidor.id'), primary_key=True)
)

#Tabela de associação entre Cliente e Endereco
cliente_endereco = Table(
    'cliente_endereco', Base.metadata,
    Column('cliente_id', Integer, ForeignKey('cliente.id'), primary_key=True),
    Column('endereco_id', Integer, ForeignKey('endereco.id'), primary_key=True)
)

#Tabela de associação entre Estoque e Produto
estoque_produto = Table(
    'estoque_produto', Base.metadata,
    Column('produto_id', Integer, ForeignKey('produto.id'), primary_key=True),
    Column('estoque_id', Integer, ForeignKey('estoque.id'), primary_key=True)
)

#Tabela de associação entre Delivre e Carrinho
delivre_carrinho = Table(
    'delivre_carrinho', Base.metadata,
    Column('delivre_id', Integer, ForeignKey('delivre.id'), primary_key=True),
    Column('carrinho_id', Integer, ForeignKey('carrinho.id'), primary_key=True)
)

#Tabela de associação entre Carrinho, Produto e Combo 
carrinho_produto = Table(
    'carrinho_produto', Base.metadata,
    Column('carrinho_id', Integer, ForeignKey('carrinho.id'), primary_key=True),
    Column('produto_id', Integer, ForeignKey('produto.id'), primary_key=True),
    Column('combo_id', Integer, ForeignKey('combo.id'), primary_key=True)
)
