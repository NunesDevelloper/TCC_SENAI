from sqlalchemy import Column, Integer
from ..db import Base

class Mesa(Base):
    __tablename__ = 'mesa'
    
    __id__ = Column(Integer, primary_key=True, autoincrement=True)
    __numero__ = Column(Integer, nullable=False)

    def __init__(self, numero: int) -> None:
        self.__numero__ = numero

    @property
    def numero(self) -> int:
        return int(self.__numero__)

    

