
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base
from .muitas_muitas import delivre_carrinho


class Delivre(Base):
    __tablename__ = 'delivre'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _nome = Column(String(255), nullable=True, name="nome")
    carrinhos = relationship("Carrinho", secondary=delivre_carrinho, backref="deliveries")

    def __init__(self, nome: str = None) -> None:
        self._nome= nome

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def nome(self) -> str:
        return str(self._nome) if self.__nome is not None else None

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self._nome = novoNome
