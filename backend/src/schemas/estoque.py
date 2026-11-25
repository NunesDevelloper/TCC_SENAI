from pydantic import BaseModel
from ..models import EnumUnidadeMedida


class BaseCriarEstoque(BaseModel):
    item_nome: str
    preco_uni: float
    quantidade: str
    fornecedor_id: int
    unidade_medida: EnumUnidadeMedida = EnumUnidadeMedida.Uni


class BaseEditarEstoque(BaseModel):
    item_nome: str | None = None
    preco_uni: float | None = None
    quantidade: str | None = None
    unidade_medida: EnumUnidadeMedida | None = None


class ResponseDadosEstoque(BaseModel):
    class DicReponse(BaseModel):
        item_nome: str
        preco_uni: float
        quantidade: str
        unidade_medida: str

    mensagem: DicReponse
