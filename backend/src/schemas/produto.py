from pydantic import BaseModel
from ..models import EnumCategoria


class BaseCriarProduto(BaseModel):
    categoria: EnumCategoria
    nome: str
    preco: float
    desc: str


class BaseEditarProduto(BaseModel):
    categoria: EnumCategoria | None = None
    nome: str | None = None
    preco: float | None = None
    desc: str | None = None


class ResponseDadosProduto(BaseModel):
    class DicReponse(BaseModel):
        categoria: str
        nome: str
        preco: str
        desc: str

    mensagem: DicReponse
