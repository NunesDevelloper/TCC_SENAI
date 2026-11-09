from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher 
from ..db import Base
from .muitas_muitas import cliente_endereco

ph = PasswordHasher()

class Cliente(Base):
    __tablename__ = 'cliente' 
    
    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _nome = Column(String(200), nullable=False, name="nome")
    _senha = Column(String(225), nullable=False, name="senha")
    _email = Column(String(225), nullable=False, name="email", unique=True)

    enderecos = relationship("Endereco", secondary=cliente_endereco, backref="clientes")

    def __init__(self, nome: str, senha: str, email: str) -> None:
        self._nome = nome
        self._senha = ph.hash(senha)
        self._email = email

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def nome(self) -> str:
        return str(self._nome)

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self._nome = novoNome

    
    def nova_senha(self, novaSenha: str) -> None:
        self._senha = ph.hash(novaSenha)

    def verificarSenha(self, senha: str) -> bool:
        return ph.verify(self._senha == senha)

    @property
    def email(self) -> str:
        return str(self._email)

    @email.setter
    def email(self, novoEmail: str) -> None:
        self._nome = novoEmail    

