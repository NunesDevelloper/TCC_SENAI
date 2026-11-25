from pydantic import BaseModel, Field
from ..models import EnumCategoria


class BaseCriarProduto(BaseModel):
    categoria: EnumCategoria
    nome: str
    preco: float
    desc: str
    estoque_ids: list[int] = Field(min_length=1)


class BaseEditarProduto(BaseModel):
    categoria: EnumCategoria | None = None
    nome: str | None = None
    preco: float | None = None
    desc: str | None = None


class BaseAssociarIngredienteProduto(BaseModel):
    produto_id: int
    estoque_id: int


class ResponseDadosProduto(BaseModel):
    class DicReponse(BaseModel):
        categoria: str
        nome: str
        preco: str
        desc: str

    mensagem: DicReponse
