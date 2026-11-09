
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from ..db import Base
from datetime import datetime


class CupomDesconto(Base):
    __tablename__ = 'cupom_desconto'

    _id = Column(Integer, primary_key=True, name="id")
    _codigo = Column(String(255), nullable=False, name="codigo")
    _percentual_desconto = Column(DECIMAL(10, 2), nullable=False, name="percentual_desconto")
    _dt_valida = Column(DateTime, nullable=False, name="dt_valida")

    def __init__(self, id: int, codigo: str, percentual_desconto: float, dt_valida: datetime) -> None:
        self._id = id
        self._codigo = codigo
        self._percentual_desconto = percentual_desconto
        self._dt_valida = dt_valida

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def codigo(self) -> str:
        return str(self._codigo)

    @codigo.setter
    def codigo(self, novoCodigo: str) -> None:
        self._codigo = novoCodigo

    @property
    def percentual_desconto(self) -> float:
        return float(self._percentual_desconto)

    @percentual_desconto.setter
    def percentual_desconto(self, novoPercentual: float) -> None:
        self._percentual_desconto = novoPercentual

    @property
    def dt_valida(self):
        return self._dt_valida

    @dt_valida.setter
    def dt_valida(self, novaData: datetime) -> None:
        self._dt_valida = novaData
