from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher 
from ..db import Base
from .muitas_muitas import cliente_endereco

ph = PasswordHasher()

class Cliente(Base):
    __tablename__ = 'cliente' 
    
    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __nome__ = Column(String(200), nullable=False, name="nome")
    __senha__ = Column(String(225), nullable=False, name="senha")
    __email__ = Column(String(225), nullable=False, name="email")

    enderecos = relationship("Endereco", secondary=cliente_endereco, backref="clientes")

    def __init__(self, nome: str, senha: str, email: str) -> None:
        self.__nome__ = nome
        self.__senha__ = ph.hash(senha)
        self.__email__ = email

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
    def senha(self, novaSenha: str) -> None:
        self.__senha__ = ph.hash(novaSenha)

    def verificarSenha(self, senha: str) -> bool:
        return ph.verify(self.__senha__ == senha)

    @property
    def email(self) -> str:
        return str(self.__email__)

    @email.setter
    def email(self, novoEmail: str) -> None:
        self.__nome__ = novoEmail    

