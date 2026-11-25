from pydantic import BaseModel


class BaseCriarFucionario(BaseModel):
    nome: str
    senha: str
    login: str


class BaseEditarFucionario(BaseModel):
    nome: str | None = None
    senha: str | None = None


class ResponseDadosFucionario(BaseModel):
    class DicReponse(BaseModel):
        nome: str
        login: str

    mensagem: DicReponse
