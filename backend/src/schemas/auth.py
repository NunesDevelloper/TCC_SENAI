from pydantic import BaseModel, EmailStr


class ResponseToken(BaseModel):
    access_token: str
    token_type: str


class BaseEmailReset(BaseModel):
    email: EmailStr


class BaseSenhaReset(BaseModel):
    senha: str