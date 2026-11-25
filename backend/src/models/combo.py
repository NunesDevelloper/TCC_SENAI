
from sqlalchemy import Column, Integer, String, DECIMAL, Text
from ..db import Base


class Combo(Base):
    __tablename__ = 'combo'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _nome = Column(String(255), nullable=False, name="nome")
    _preco = Column(DECIMAL(10, 2), nullable=False, name="preco")
    _descricao = Column(Text, nullable=True, name="desc")

    def __init__(self, nome: str, preco: float, desc: str = None) -> None:
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
        self._nome = novoNome

    @property
    def preco(self) -> float:
        return float(self._preco)

    @preco.setter
    def preco(self, novoPreco: float) -> None:
        self._preco = novoPreco

    @property
    def desc(self) -> str:
        return str(self._descricao)

    @desc.setter
    def desc(self, novaDesc: str) -> None:
        self._descricao = novaDesc