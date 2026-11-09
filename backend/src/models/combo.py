
from sqlalchemy import Column, Integer, String, DECIMAL, Text
from ..db import Base


class Combo(Base):
    __tablename__ = 'combo'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __nome__ = Column(String(255), nullable=False, name="nome")
    __preco__ = Column(DECIMAL(10, 2), nullable=False, name="preco")
    __descricao__ = Column(Text, nullable=True, name="desc")

    def __init__(self, nome: str, preco: float, desc: str = None) -> None:
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
    def preco(self) -> float:
        return float(self.__preco__)

    @preco.setter
    def preco(self, novoPreco: float) -> None:
        self.__preco__ = novoPreco

    @property
    def desc(self) -> str:
        return str(self.__descricao__)

    @desc.setter
    def desc(self, novaDesc: str) -> None:
        self.__descricao__ = novaDesc