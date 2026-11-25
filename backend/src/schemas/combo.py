from decimal import Decimal
from pydantic import BaseModel


class BaseCriarCombo(BaseModel):
    nome: str
    preco: float
    desc: str | None = None


class BaseEditarCombo(BaseModel):
    nome: str | None = None
    preco: float | None = None
    desc: str | None = None


class ResponseDadosCombo(BaseModel):
    class DicReponse(BaseModel):
        nome: str
        preco: Decimal
        desc: str | None

    mensagem: DicReponse
