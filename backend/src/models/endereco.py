
from sqlalchemy import Column, Integer, String, Text
from ..db import Base


class Endereco(Base):
    __tablename__ = 'endereco'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __logradouro__ = Column(String(125), nullable=False, name="logradouro")
    __numero__ = Column(Integer, nullable=True, name="numero")
    __complemento__ = Column(Text, nullable=True, name="complemento")
    __bairro__ = Column(String(120), nullable=False, name="bairro")
    __cep__ = Column(String(120), nullable=False, name="cep")

    def __init__(self,logradouro: str,bairro: str,cep: str, numero: int = None, complemento: str = None) -> None:
        self.__logradouro__ = logradouro
        self.__numero__ = numero
        self.__complemento__ = complemento
        self.__bairro__ = bairro
        self.__cep__ = cep

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def logradouro(self) -> str:
        return str(self.__logradouro__)

    @logradouro.setter
    def logradouro(self, novoLogradouro: str) -> None:
        self.__logradouro__ = novoLogradouro

    @property
    def numero(self) -> int:
        return self.__numero__

    @numero.setter
    def numero(self, novoNumero: int) -> None:
        self.__numero__ = novoNumero

    @property
    def complemento(self) -> str:
        return self.__complemento__

    @complemento.setter
    def complemento(self, novoComplemento: str) -> None:
        self.__complemento__ = novoComplemento

    @property
    def bairro(self) -> str:
        return str(self.__bairro__)

    @bairro.setter
    def bairro(self, novoBairro: str) -> None:
        self.__bairro__ = novoBairro

    @property
    def cep(self) -> str:
        return str(self.__cep__)

    @cep.setter
    def cep(self, novoCep: str) -> None:
        self.__cep__ = novoCep
