from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import Cliente
from .erros import DuplicationUser, RequestInvalida ,NoteUserSenha, ErroInesperado, DnsEmailNotExiste
from .email import is_valido_dns

def criar_conta_cliente(nome: str, senha: str, email: str, session : Session) -> dict:
    try:
        if is_valido_dns(email) == False: raise DnsEmailNotExiste() 

        user : Cliente 

        user = Cliente(nome, senha , email) 
    
        session.add(user)
        session.commit()
        return {'mensagem': 'cliente criado com sucesso'}
    
    except (DnsEmailNotExiste):
        raise

    except IntegrityError:
        raise DuplicationUser(session)
    
    except Exception as e:
        raise ErroInesperado(e, session)

def del_acont_cliente(id: int, session: Session) -> dict:
    try:

        query = session.query(Cliente).filter_by(_id = id).delete() 

        if query:
            session.commit()
            return {"mensagem": "cliente removido."}
        else: raise NoteUserSenha(session)

    except (NoteUserSenha) : raise

    except Exception as e:
        raise ErroInesperado(e, session)

def alterar_dados_cliente(id: int, senha: str  | None, nome: str | None, session: Session) -> dict:
    try:
        query = session.query(Cliente).filter_by(_id = id).first()

        if query:
            if senha != None : query.nova_senha(senha)  
             
            if nome != None: query.nome = nome 

            if nome is None and senha is None: raise RequestInvalida(session)

        else: raise NoteUserSenha(session)

        session.commit()
        return {'mensagem': 'cliente editado com sucesso.'}

    except (NoteUserSenha, RequestInvalida) : raise

    except Exception as e:
        raise ErroInesperado(e, session)

def dados_cliente(id: int, session: Session):
    try:
        query = session.query(Cliente).filter_by(_id = id).first()

        if query is not None:
            return {
                'mensagem':{
                    'nome' : query.nome,
                    'email' : query.email
                }
            }
        else: raise NoteUserSenha(session)
    
    except (NoteUserSenha): raise

    except Exception as e:
        raise ErroInesperado(e, session) 


