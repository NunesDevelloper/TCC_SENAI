from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class BaseCriarCupomDesconto(BaseModel):
    id: int
    codigo: str
    percentual_desconto: float
    dt_valida: datetime


class BaseEditarCupomDesconto(BaseModel):
    codigo: str | None = None
    percentual_desconto: float | None = None
    dt_valida: datetime | None = None


class ResponseDadosCupomDesconto(BaseModel):
    class DicReponse(BaseModel):
        codigo: str
        percentual_desconto: Decimal
        dt_valida: datetime

    mensagem: DicReponse
