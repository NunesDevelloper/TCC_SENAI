
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..db import Base
from .muitas_muitas import estoque_fornecidor

class Fornecedor(Base):
    __tablename__ = 'fornecidor'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _cnpj= Column(String(100), nullable=False, name="cnpj")
    _nome = Column(String(100), nullable=False, name="nome")
    _contato = Column(Text, nullable=False, name="contado")

    estoques = relationship("Estoque", secondary=estoque_fornecidor, backref="fornecedores")

    def __init__(self, cnpj: str, nome: str, contato: str) -> None:
        self._cnpj = cnpj
        self._nome = nome
        self._contato = contato

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def cnpj(self) -> str:
        return str(self._cnpj)

    @cnpj.setter
    def cnpj(self, novoCnpj: str) -> None:
        self._cnpj = novoCnpj

    @property
    def nome(self) -> str:
        return str(self._nome)

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self._nome = novoNome

    @property
    def contato(self) -> str:
        return str(self._contato)

    @contato.setter
    def contato(self, novoContato: str) -> None:
        self._contato = novoContato
