from sqlalchemy.orm import Session
from ..models import Cliente, Funcionario
from .erros import NoteFucionarioSenha ,NoteUserSenha, ErroInesperado
from .jwt import criar_token

def logar_conta(login: str, senha: str, session: Session) -> dict :
    try:    
        query_c = session.query(Cliente).filter_by(_email = login).first()  # type: ignore
        query_f = session.query(Funcionario).filter_by(_login = login).first()  # type: ignore


        if query_f is None and query_c is None: raise NoteUserSenha(session)

        if query_f is None:
            if query_c.verificarSenha(senha):
                _jwt = criar_token(query_c.id, None, False)

            else: raise NoteUserSenha(session)
        else:
            if query_f.verificarSenha(senha):
                _jwt = criar_token(query_f.id, is_fucioanrio=True)
            
            else: raise NoteFucionarioSenha(session)


        return {
                "access_token": _jwt,
                "token_type": "bearer"
            }

    except (NoteUserSenha, NoteFucionarioSenha): raise

    except Exception as e:
        raise ErroInesperado(e, session)


