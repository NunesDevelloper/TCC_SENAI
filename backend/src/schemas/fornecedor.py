from pydantic import BaseModel


class BaseCriarFornecedor(BaseModel):
    cnpj: str
    nome: str
    contato: str


class BaseEditarFornecedor(BaseModel):
    cnpj: str | None = None
    nome: str | None = None
    contato: str | None = None


class ResponseDadosFornecedor(BaseModel):
    class DicReponse(BaseModel):
        cnpj: str
        nome: str
        contato: str

    mensagem: DicReponse
