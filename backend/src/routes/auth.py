from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..db import get_sesion
from ..schemas import BaseEmailReset, BaseSenhaReset, ResponseOk, ResponseToken
from ..services import enviar_email, logar_conta, verificar_email_senha

Rotas_Auth = APIRouter(
    responses={
        401: {"description": "Token inválido ou expirado"},
        404: {"description": "Credenciais inválidas ou cliente não encontrado"},
        503: {"description": "Servidor de e-mail indisponível"}
    }
)


@Rotas_Auth.post("/login_conta", response_model=ResponseToken)
async def login_conta(base: OAuth2PasswordRequestForm = Depends(), 
                      session: Session = Depends(get_sesion)):
    
    return logar_conta(base.username, base.password, session)


@Rotas_Auth.post("/solicitar_reset_senha", response_model=ResponseOk)
async def solicitar_reset_senha(base: BaseEmailReset,session: Session = Depends(get_sesion)):
    return await enviar_email(base.email, session)


@Rotas_Auth.put("/resetar_senha/{token}", response_model=ResponseOk)
async def resetar_senha(token: str,base: BaseSenhaReset,session: Session = Depends(get_sesion)):
    return await verificar_email_senha(token, base.senha, session)


