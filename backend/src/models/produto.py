from sqlalchemy import Column, Integer, String, Enum, DECIMAL, Text
from ..db import Base
from enum import Enum as enum

class EnumCategoria(enum):
    lanche = 'lanche' 
    bebida ='bebida' 
    porcoe = 'porcoe' 
    sobremesa ='sobremesa'


class Produto(Base):
    __tablename__ = 'produto'
    
    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _categoria = Column(Enum(EnumCategoria), nullable=False, name="categoria")
    _nome = Column(String(255), nullable=False, name="nome")
    _preco= Column(DECIMAL(10, 2), nullable=False, name="preco")
    _descricao = Column(Text, nullable=True, name="desc")

    def __init__(self, categoria: EnumCategoria, nome: str, preco: float, desc: str) -> None:
        self._categoria = categoria
        self._nome = nome
        self._preco = preco
        self._descricao = desc

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def nome(self) -> str:
        return str(self._nome)

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self__nome= novoNome

    @property
    def categoria(self) -> str:
        return str(self._categoria)

    @categoria.setter
    def categoria(self, novocategoria: EnumCategoria) -> None:
        self._categoria= novocategoria

    @property
    def preco(self) -> str:
        return str(self._preco)

    @preco.setter
    def preco(self, novopreco: int) -> None:
        self._preco= novopreco

    @property
    def desc(self) -> str:
        return str(self._descricao)

    @desc.setter
    def desc(self, novodesc: str) -> None:
        self._descricao= novodesc

    


    
