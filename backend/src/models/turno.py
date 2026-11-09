from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from datetime import datetime
from ..db import Base
import enum

class EnumCargo(enum):
    atendente: str = 'atendente' 
    cozinheiro: str = 'cozinheiro'
    entregador: str = 'entregador' 
    gerente : str = 'gerente'
    
class Turno(Base):
    __tablename__ = 'turno'
    
    __id__ = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __cargo__ = Column(Enum(EnumCargo), nullable=False, name="cargo")
    __dt_inicio__ = Column(DateTime, nullable=False, default=datetime.now(), name="dt_inicio")
    __dt_final__ = Column(DateTime, nullable=True, name="dt_final")
    
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'), primary_key=True)

    def __init__(self, cargo: EnumCargo,  dt_final: datetime , dt_inicio : datetime = datetime.now ) -> None:
        self.__cargo__ = cargo
        self.__dt_final__ = dt_final
        self.__dt_inicio__ = dt_inicio

    @property
    def id(self) -> int:
        return int(self.__id__)

    @property
    def cargo(self) -> str:
        return str(self.__cargo__)

    @cargo.setter
    def cargo(self, novoCargo: EnumCargo) -> None:
        self.__cargo__ = novoCargo

    @property
    def dt_inicial(self) -> datetime:
        return self.__dt_inicial__

    @property
    def dt_final(self) -> datetime | None:
        return self.__dt_inicial__   

    @dt_final.setter
    def dt_final(self, dt_final: datetime) -> datetime:
        self.__dt_final__ = dt_final


