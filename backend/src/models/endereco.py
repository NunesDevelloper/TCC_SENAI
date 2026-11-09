
from sqlalchemy import Column, Integer, String, Text
from ..db import Base


class Endereco(Base):
    __tablename__ = 'endereco'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _logradouro= Column(String(125), nullable=False, name="logradouro")
    _numero = Column(Integer, nullable=True, name="numero")
    _complemento = Column(Text, nullable=True, name="complemento")
    _bairro = Column(String(120), nullable=False, name="bairro")
    _cep = Column(String(120), nullable=False, name="cep")

    def __init__(self,logradouro: str,bairro: str,cep: str, numero: int = None, complemento: str = None) -> None:
        self._logradouro = logradouro
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._cep = cep

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def logradouro(self) -> str:
        return str(self._logradouro)

    @logradouro.setter
    def logradouro(self, novoLogradouro: str) -> None:
        self._logradouro= novoLogradouro

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, novoNumero: int) -> None:
        self._numero = novoNumero

    @property
    def complemento(self) -> str:
        return self._complemento

    @complemento.setter
    def complemento(self, novoComplemento: str) -> None:
        self._complemento= novoComplemento

    @property
    def bairro(self) -> str:
        return str(self._bairro)

    @bairro.setter
    def bairro(self, novoBairro: str) -> None:
        self._bairro= novoBairro

    @property
    def cep(self) -> str:
        return str(self._cep)

    @cep.setter
    def cep(self, novoCep: str) -> None:
        self._cep= novoCep
