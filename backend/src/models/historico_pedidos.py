
from sqlalchemy import Column, Integer, ForeignKey, Enum
from enum import Enum as enum
from ..db import Base

class EnumHistorico(enum):
    pago='pago' 
    preparo='preparo'
    pronto='pronto' 
    entregue='entregue'
    cancelado='cancelado'

class HistoricoPedidos(Base):
    __tablename__ = 'historico_pedidos'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _carrinho_id = Column(Integer, ForeignKey('carrinho.id'), name="carrinho_id")
    _status = Column(Enum(EnumHistorico), nullable=False,default=EnumHistorico.preparo,name="status")

    def __init__(self,carrinho_id: int,status: EnumHistorico = EnumHistorico.preparo) -> None:
        self._carrinho_id = carrinho_id
        self._status = status

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def carrinho_id(self) -> int:
        return int(self._carrinho_id)

    @property
    def status(self) -> str:
        return self._status.value

    @status.setter
    def status(self, novoStatus: EnumHistorico) -> None:
        self._status = novoStatus
