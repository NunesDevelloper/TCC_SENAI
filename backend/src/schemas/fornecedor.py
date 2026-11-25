from pydantic import BaseModel


class BaseCriarFornecedor(BaseModel):
    cnpj: str
    nome: str
    contato: str


class BaseEditarFornecedor(BaseModel):
    cnpj: str | None = None
    nome: str | None = None
    contato: str | None = None


class BaseAssociarFornecedorEstoque(BaseModel):
    fornecedor_id: int
    estoque_id: int


class ResponseDadosFornecedor(BaseModel):
    class DicReponse(BaseModel):
        cnpj: str
        nome: str
        contato: str

    mensagem: DicReponse
