from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher 
from ..db import Base

ph = PasswordHasher()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    
    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _nome = Column(String(120), nullable=False, name="nome")
    _login = Column(String(255), nullable=False, name="login")
    _senha = Column(String(255), nullable=False, name="senha")
    
    turnos = relationship("Turno", backref="funcionario")

    def __init__(self, nome: str, login: str, senha: str) -> None:
        self._nome =  nome
        self._login = login
        self._senha = ph.hash(senha)

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
    def senha(self, novaSenha: str) -> None:
        self._senha = ph.hash(novaSenha)

    def verificarSenha(self, senha: str) -> bool:
        return ph.verify(self._senha == senha)

    @property
    def login(self) -> str:
        return str(self._login)

    @login.setter
    def email(self, novoLogin: str) -> None:
        self._login = novoLogin    

    
