from pydantic import BaseModel


class BaseCriarDelivre(BaseModel):
    nome: str | None = None


class BaseEditarDelivre(BaseModel):
    nome: str | None = None


class BaseAssociarPedidoDelivre(BaseModel):
    delivre_id: int
    carrinho_id: int


class ResponseDadosDelivre(BaseModel):
    class DicReponse(BaseModel):
        nome: str | None

    mensagem: DicReponse
