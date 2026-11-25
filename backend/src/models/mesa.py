from sqlalchemy import Column, Integer
from ..db import Base

class Mesa(Base):
    __tablename__ = 'mesa'
    
    _id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    _numero = Column(Integer, nullable=False, name="numero")

    def __init__(self, numero: int) -> None:
        self._numero = numero

    @property
    def id(self) -> int:
        return int(self._id)

    @property
    def numero(self) -> int:
        return int(self._numero)

    

