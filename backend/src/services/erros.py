from fastapi import HTTPException, status
from sqlalchemy.orm import Session

class DuplicationUser(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='já existe um cliente com esse email'
        )

class NoteUserSenha(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há User Verificado com esse Email"
        )

class ErroInesperado(HTTPException):
    def __init__(self, e, session: Session | None = None):
        if session is not None:
            session.rollback()

        super().__init__(
            status_code=500,
            detail=f"Erro inesperado do servidor.Erro -> {e}"
        )

class DnsEmailNotExiste(HTTPException):
    def __init__(self):

        super().__init__(
            status_code=422,
            detail= "Dns do email não existe"
        )


class RequestInvalida(HTTPException):
    def __init__(self, session: Session | None = None):
        
        if session is not None: session.rollback()

        super().__init__(
            status_code=422,
            detail= "Nem um campo devidamente informado"
        )

    