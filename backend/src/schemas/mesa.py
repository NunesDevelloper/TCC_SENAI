from pydantic import BaseModel


class BaseCriarMesa(BaseModel):
    numero: int


class BaseEditarMesa(BaseModel):
    numero: int | None = None


class ResponseDadosMesa(BaseModel):
    class DicReponse(BaseModel):
        numero: int

    mensagem: DicReponse
