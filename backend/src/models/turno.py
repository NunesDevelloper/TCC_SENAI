from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from datetime import datetime
from ..db import Base
from enum import Enum as enum

class EnumCargo(enum):
    atendente: str = 'atendente' 
    cozinheiro: str = 'cozinheiro'
    entregador: str = 'entregador' 
    gerente : str = 'gerente'
    
class Turno(Base):
    __tablename__ = 'turno'
    
    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _cargo= Column(Enum(EnumCargo), nullable=False, name="cargo")
    _dt_inicio = Column(DateTime, nullable=False, default=datetime.now(), name="dt_inicio")
    _dt_final = Column(DateTime, nullable=True, name="dt_final")
    
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'), primary_key=True)

    def __init__(self, cargo: EnumCargo,  dt_final: datetime , dt_inicio : datetime = datetime.now ) -> None:
        self._cargo = cargo
        self._dt_final = dt_final
        self._dt_inicio = dt_inicio

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def cargo(self) -> str:
        return str(self._cargo)

    @cargo.setter
    def cargo(self, novoCargo: EnumCargo) -> None:
        self._cargo = novoCargo

    @property
    def dt_inicial(self) -> datetime:
        return self._dt_inicial

    @property
    def dt_final(self) -> datetime | None:
        return self._dt_inicial   

    @dt_final.setter
    def dt_final(self, dt_final: datetime) -> datetime:
        self._dt_final = dt_final


