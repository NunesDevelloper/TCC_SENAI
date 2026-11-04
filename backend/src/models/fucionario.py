from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher 
from ..db import Base

ph = PasswordHasher()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    
    __id__ = Column(Integer, primary_key=True, autoincrement=True)
    __nome__ = Column(String(120), nullable=False)
    __login__ = Column(String(255), nullable=False)
    __senha__ = Column(String(255), nullable=False)
    
    turnos = relationship("Turno", backref="funcionario")

    def __init__(self, nome: str, login: str, senha: str) -> None:
        self.__nome__ =  nome
        self.__login__ = login
        self.__senha__ = ph.hash(senha)

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
    def login(self) -> str:
        return str(self.__login__)

    @login.setter
    def email(self, novoLogin: str) -> None:
        self.__login__ = novoLogin    

    def __call__(self) -> dict:
        return {
            "mensagem":{
                "id": self.id,
                "nome": self.nome, 
                "email": self.login
                }
            }

    
