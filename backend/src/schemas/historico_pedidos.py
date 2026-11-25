from pydantic import BaseModel
from ..models import EnumHistorico


class BaseCriarHistoricoPedidos(BaseModel):
    carrinho_id: int
    status: EnumHistorico = EnumHistorico.preparo


class BaseEditarHistoricoPedidos(BaseModel):
    carrinho_id: int | None = None
    status: EnumHistorico | None = None


class ResponseDadosHistoricoPedidos(BaseModel):
    class DicReponse(BaseModel):
        carrinho_id: int
        status: str

    mensagem: DicReponse
