
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from ..db import Base
from datetime import datetime


class CupomDesconto(Base):
    __tablename__ = 'cupom_desconto'

    __id__ = Column(Integer, primary_key=True, name="id")
    __codigo__ = Column(String(255), nullable=False, name="codigo")
    __percentual_desconto__ = Column(DECIMAL(10, 2), nullable=False, name="percentual_desconto")
    __dt_valida__ = Column(DateTime, nullable=False, name="dt_valida")

    def __init__(self, id: int, codigo: str, percentual_desconto: float, dt_valida: datetime) -> None:
        self.__id__ = id
        self.__codigo__ = codigo
        self.__percentual_desconto__ = percentual_desconto
        self.__dt_valida__ = dt_valida

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def codigo(self) -> str:
        return str(self.__codigo__)

    @codigo.setter
    def codigo(self, novoCodigo: str) -> None:
        self.__codigo__ = novoCodigo

    @property
    def percentual_desconto(self) -> float:
        return float(self.__percentual_desconto__)

    @percentual_desconto.setter
    def percentual_desconto(self, novoPercentual: float) -> None:
        self.__percentual_desconto__ = novoPercentual

    @property
    def dt_valida(self):
        return self.__dt_valida__

    @dt_valida.setter
    def dt_valida(self, novaData: datetime) -> None:
        self.__dt_valida__ = novaData
