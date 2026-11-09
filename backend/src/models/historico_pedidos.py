
from sqlalchemy import Column, Integer, ForeignKey, Enum
from ..db import Base

class HistoricoPedidos(Base):
    __tablename__ = 'historico_pedidos'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __carrinho_id__ = Column(Integer, ForeignKey('carrinho.id'), primary_key=True, name="carrinho_id")
    __status__ = Column(
        Enum('pago', 'preparo', 'pronto', 'entregue', 'cancelado', name='status_enum'),
        nullable=False,
        default='preparo',
        name="status"
    )

    def __init__(self, carrinho_id: int, status: str = 'preparo') -> None:
        self.__carrinho_id__ = carrinho_id
        self.__status__ = status

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def carrinho_id(self) -> int:
        return int(self.__carrinho_id__)

    @property
    def status(self) -> str:
        return str(self.__status__)

    @status.setter
    def status(self, novoStatus: str) -> None:
        self.__status__ = novoStatus
