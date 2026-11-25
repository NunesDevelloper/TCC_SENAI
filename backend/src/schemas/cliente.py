from pydantic import BaseModel, EmailStr

class BaseCriarCliente(BaseModel):
    nome: str
    senha: str
    email: EmailStr


class BaseEditarCliente(BaseModel):
    #Igualar a None gera um campo opcional, ou seja, se ele não for passado, o código continua
    nome: str | None = None
    senha: str | None = None


class ResponseDadosCliente(BaseModel):
    #isso server como uma reprecentação de -> {}
    class DicReponse(BaseModel):
        nome: str
        email : str

    mensagem: DicReponse

