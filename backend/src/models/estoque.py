
from sqlalchemy import Column, Integer, String, Enum, DECIMAL
from sqlalchemy.orm import relationship
from ..db import Base
from .muitas_muitas import estoque_produto
import enum

class EnumUnidadeMedida(enum):
    Kg = 'Kg', 
    L = 'L', 
    Uni = 'Uni'



class Estoque(Base):
    __tablename__ = 'estoque'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __item_nome__ = Column(String(225), nullable=False, name="intem_nome")
    __preco_uni__ = Column(DECIMAL(10, 2), nullable=False, name="preco_uni")
    __quantidade__ = Column(String(225), nullable=False, name="quantidade")
    __unidade_medida__ = Column(Enum(EnumUnidadeMedida),nullable=False,default=EnumUnidadeMedida.Uni,name="unidade_medida")

    produtos = relationship("Produto", secondary=estoque_produto, backref="estoques")

    def __init__(self, item_nome: str, preco_uni: float, quantidade: str, unidade_medida: str = 'Uni') -> None:
        self.__item_nome__ = item_nome
        self.__preco_uni__ = preco_uni
        self.__quantidade__ = quantidade
        self.__unidade_medida__ = unidade_medida

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def item_nome(self) -> str:
        return str(self.__item_nome__)

    @item_nome.setter
    def item_nome(self, novoNome: str) -> None:
        self.__item_nome__ = novoNome

    @property
    def preco_uni(self) -> float:
        return float(self.__preco_uni__)

    @preco_uni.setter
    def preco_uni(self, novoPreco: float) -> None:
        self.__preco_uni__ = novoPreco

    @property
    def quantidade(self) -> str:
        return str(self.__quantidade__)

    @quantidade.setter
    def quantidade(self, novaQuantidade: str) -> None:
        self.__quantidade__ = novaQuantidade

    @property
    def unidade_medida(self) -> str:
        return str(self.__unidade_medida__)

    @unidade_medida.setter
    def unidade_medida(self, novaUnidade: EnumUnidadeMedida) -> None:
        self.__unidade_medida__ = novaUnidade
