
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..db import Base
from .muitas_muitas import estoque_fornecedor


class Fornecedor(Base):
    __tablename__ = 'fornecidor'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __cnpj__ = Column(String(100), nullable=False, name="cnpj")
    __nome__ = Column(String(100), nullable=False, name="nome")
    __contato__ = Column(Text, nullable=False, name="contado")

    estoques = relationship("Estoque", secondary=estoque_fornecedor, backref="fornecedores")

    def __init__(self, cnpj: str, nome: str, contato: str) -> None:
        self.__cnpj__ = cnpj
        self.__nome__ = nome
        self.__contato__ = contato

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def cnpj(self) -> str:
        return str(self.__cnpj__)

    @cnpj.setter
    def cnpj(self, novoCnpj: str) -> None:
        self.__cnpj__ = novoCnpj

    @property
    def nome(self) -> str:
        return str(self.__nome__)

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome__ = novoNome

    @property
    def contato(self) -> str:
        return str(self.__contato__)

    @contato.setter
    def contato(self, novoContato: str) -> None:
        self.__contato__ = novoContato
