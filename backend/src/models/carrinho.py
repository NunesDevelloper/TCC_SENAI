
from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base
from enum import Enum as enum

class EnumMetedoPagamento(enum):
    dinheiro ='dinheiro' 
    pix ='pix'
    credito = 'credito' 
    debito = 'debito'


class Carrinho(Base):
    __tablename__ = 'carrinho'

    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _is_delivre = Column(Boolean, nullable=False, default=False, name="is_delivre")
    _is_retirada = Column(Boolean, nullable=False, default=False, name="is_retirada")
    _metedo_pagamento = Column(Enum(EnumMetedoPagamento),nullable=False,default= EnumMetedoPagamento.pix,
        name="metedo_pagamento"
    )
    _cliente_id = Column(Integer, ForeignKey('cliente.id'), primary_key=True)
    _funcionario_id = Column(Integer, ForeignKey('funcionario.id'), primary_key=True)
    _mesa_id = Column(Integer, ForeignKey('mesa.id'), primary_key=True)
    _cupom_desconto_id = Column(Integer, ForeignKey('cupom_desconto.id'), primary_key=True)

    historico = relationship("HistoricoPedidos", backref="carrinho")

    def __init__(self,cliente_id: int,funcionario_id: int,mesa_id: int,cupom_desconto_id: int,is_delivre: bool = False,
                 is_retirada: bool = False,metedo_pagamento: EnumMetedoPagamento = EnumMetedoPagamento.pix) -> None:
        self._cliente_id = cliente_id
        self._funcionario_id = funcionario_id
        self._mesa_id = mesa_id
        self._cupom_desconto_id = cupom_desconto_id
        self._is_delivre = is_delivre
        self._is_retirada = is_retirada
        self._metedo_pagamento = metedo_pagamento

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def is_delivre(self) -> bool:
        return bool(self._is_delivre)

    @is_delivre.setter
    def is_delivre(self, valor: bool) -> None:
        self._is_delivre = valor

    @property
    def is_retirada(self) -> bool:
        return bool(self._is_retirada)

    @is_retirada.setter
    def is_retirada(self, valor: bool) -> None:
        self._is_retirada = valor

    @property
    def metedo_pagamento(self) -> str:
        return str(self._metedo_pagamento)

    @metedo_pagamento.setter
    def metedo_pagamento(self, novoMetedo: EnumMetedoPagamento) -> None:
        self._metedo_pagamento = novoMetedo
