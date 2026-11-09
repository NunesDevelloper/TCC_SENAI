
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base
from .muitas_muitas import delivre_carrinho


class Delivre(Base):
    __tablename__ = 'delivre'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __nome__ = Column(String(255), nullable=True, name="nome")

    carrinhos = relationship("Carrinho", secondary=delivre_carrinho, backref="deliveries")

    def __init__(self, nome: str = None) -> None:
        self.__nome__ = nome

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def nome(self) -> str:
        return str(self.__nome__) if self.__nome__ is not None else None

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome__ = novoNome
