from sqlalchemy import Column, Integer, String, Enum, DECIMAL, Text
from ..db import Base
import enum

class EnumCategoria(enum):
    lanche = 'lanche' 
    bebida ='bebida' 
    porcoe = 'porcoe' 
    sobremesa ='sobremesa'


class Produto(Base):
    __tablename__ = 'produto'
    
    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __categoria__ = Column(Enum(EnumCategoria), nullable=False, name="categoria")
    __nome__ = Column(String(255), nullable=False, name="nome")
    __preco__= Column(DECIMAL(10, 2), nullable=False, name="preco")
    __descricao__ = Column(Text, nullable=True, name="desc")

    def __init__(self, categoria: EnumCategoria, nome: str, preco: float, desc: str) -> None:
        self.__categoria__ = categoria
        self.__nome__ = nome
        self.__preco__ = preco
        self.__descricao__ = desc

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def nome(self) -> str:
        return str(self.__nome__)

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome__ = novoNome

    @property
    def categoria(self) -> str:
        return str(self.__categoria__)

    @categoria.setter
    def categoria(self, novocategoria: EnumCategoria) -> None:
        self.__categoria__ = novocategoria

    @property
    def preco(self) -> str:
        return str(self.__preco__)

    @preco.setter
    def preco(self, novopreco: int) -> None:
        self.__preco__ = novopreco

    @property
    def desc(self) -> str:
        return str(self.__descricao__)

    @desc.setter
    def desc(self, novodesc: str) -> None:
        self.__descricao__ = novodesc

    


    
