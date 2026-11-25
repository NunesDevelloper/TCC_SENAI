from pydantic import BaseModel


class BaseCriarDelivre(BaseModel):
    nome: str | None = None


class BaseEditarDelivre(BaseModel):
    nome: str | None = None


class ResponseDadosDelivre(BaseModel):
    class DicReponse(BaseModel):
        nome: str | None

    mensagem: DicReponse
