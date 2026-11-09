
from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base
import enum

class EnumMetedoPagamento(enum):
    dinheiro ='dinheiro' 
    pix ='pix'
    credito = 'credito' 
    debito = 'debito'


class Carrinho(Base):
    __tablename__ = 'carrinho'

    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __is_delivre__ = Column(Boolean, nullable=False, default=False, name="is_delivre")
    __is_retirada__ = Column(Boolean, nullable=False, default=False, name="is_retirada")
    __metedo_pagamento__ = Column(Enum(EnumMetedoPagamento),nullable=False,default= EnumMetedoPagamento.pix,
        name="metedo_pagamento"
    )
    __cliente_id__ = Column(Integer, ForeignKey('cliente.id'), primary_key=True)
    __funcionario_id__ = Column(Integer, ForeignKey('funcionario.id'), primary_key=True)
    __mesa_id__ = Column(Integer, ForeignKey('mesa.id'), primary_key=True)
    __cupom_desconto_id__ = Column(Integer, ForeignKey('cupom_desconto.id'), primary_key=True)

    historico = relationship("HistoricoPedidos", backref="carrinho")

    def __init__(self,cliente_id: int,funcionario_id: int,mesa_id: int,cupom_desconto_id: int,is_delivre: bool = False,
                 is_retirada: bool = False,metedo_pagamento: EnumMetedoPagamento = EnumMetedoPagamento.pix) -> None:
        self.__cliente_id__ = cliente_id
        self.__funcionario_id__ = funcionario_id
        self.__mesa_id__ = mesa_id
        self.__cupom_desconto_id__ = cupom_desconto_id
        self.__is_delivre__ = is_delivre
        self.__is_retirada__ = is_retirada
        self.__metedo_pagamento__ = metedo_pagamento

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def is_delivre(self) -> bool:
        return bool(self.__is_delivre__)

    @is_delivre.setter
    def is_delivre(self, valor: bool) -> None:
        self.__is_delivre__ = valor

    @property
    def is_retirada(self) -> bool:
        return bool(self.__is_retirada__)

    @is_retirada.setter
    def is_retirada(self, valor: bool) -> None:
        self.__is_retirada__ = valor

    @property
    def metedo_pagamento(self) -> str:
        return str(self.__metedo_pagamento__)

    @metedo_pagamento.setter
    def metedo_pagamento(self, novoMetedo: EnumMetedoPagamento) -> None:
        self.__metedo_pagamento__ = novoMetedo
