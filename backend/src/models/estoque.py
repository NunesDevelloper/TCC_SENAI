
from sqlalchemy import Column, Integer, String, Enum, DECIMAL
from sqlalchemy.orm import relationship
from ..db import Base
from .muitas_muitas import estoque_produto
from enum import Enum as enum

class EnumUnidadeMedida(enum):
    Kg = 'Kg', 
    L = 'L', 
    Uni = 'Uni'



class Estoque(Base):
    __tablename__ = 'estoque'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _item_nome = Column(String(225), nullable=False, name="intem_nome")
    _preco_uni = Column(DECIMAL(10, 2), nullable=False, name="preco_uni")
    _quantidade = Column(String(225), nullable=False, name="quantidade")
    _unidade_medida = Column(Enum(EnumUnidadeMedida),nullable=False,default=EnumUnidadeMedida.Uni,name="unidade_medida")

    produtos = relationship("Produto", secondary=estoque_produto, backref="estoques")

    def __init__(self, item_nome: str, preco_uni: float, quantidade: str, unidade_medida: str = 'Uni') -> None:
        self._item_nome = item_nome
        self._preco_uni = preco_uni
        self._quantidade = quantidade
        self._unidade_medida = unidade_medida

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def item_nome(self) -> str:
        return str(self._item_nome)

    @item_nome.setter
    def item_nome(self, novoNome: str) -> None:
        self._item_nome= novoNome

    @property
    def preco_uni(self) -> float:
        return float(self._preco_uni)

    @preco_uni.setter
    def preco_uni(self, novoPreco: float) -> None:
        self._preco_uni = novoPreco

    @property
    def quantidade(self) -> str:
        return str(self._quantidade)

    @quantidade.setter
    def quantidade(self, novaQuantidade: str) -> None:
        self._quantidade = novaQuantidade

    @property
    def unidade_medida(self) -> str:
        return str(self._unidade_medida)

    @unidade_medida.setter
    def unidade_medida(self, novaUnidade: EnumUnidadeMedida) -> None:
        self._unidade_medida = novaUnidade
