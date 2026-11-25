from pydantic import BaseModel


class BaseCriarHistoricoPedidos(BaseModel):
    carrinho_id: int
    status: str = "preparo"


class BaseEditarHistoricoPedidos(BaseModel):
    carrinho_id: int | None = None
    status: str | None = None


class ResponseDadosHistoricoPedidos(BaseModel):
    class DicReponse(BaseModel):
        carrinho_id: int
        status: str

    mensagem: DicReponse
