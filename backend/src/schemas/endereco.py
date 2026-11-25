from pydantic import BaseModel


class BaseCriarEndereco(BaseModel):
    logradouro: str
    bairro: str
    cep: str
    numero: int | None = None
    complemento: str | None = None


class BaseEditarEndereco(BaseModel):
    logradouro: str | None = None
    bairro: str | None = None
    cep: str | None = None
    numero: int | None = None
    complemento: str | None = None


class ResponseDadosEndereco(BaseModel):
    class DicReponse(BaseModel):
        logradouro: str
        numero: int | None
        complemento: str | None
        bairro: str
        cep: str

    mensagem: DicReponse
