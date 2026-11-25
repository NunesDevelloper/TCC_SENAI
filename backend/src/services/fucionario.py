from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import Funcionario
from .erros import DuplicationFucionario, RequestInvalida ,NoteFucionarioSenha , ErroInesperado

def criar_conta_fucionario(nome: str, senha: str, login: str, session : Session) -> dict:
    try:
        user : Funcionario 

        user = Funcionario(nome, senha , login) 
    
        session.add(user)
        session.commit()
        return {'mensagem': 'fucionaro criado com sucesso'}   

    except IntegrityError:
        raise DuplicationFucionario(session)
    
    except Exception as e:
        raise ErroInesperado(e, session)

def del_acont_fucionario(id: int, session: Session) -> dict:
    try:

        query = session.query(Funcionario).filter_by(_id = id).delete() 

        if query:
            session.commit()
            return {"mensagem": "fucionaro removido."}
        else: raise NoteFucionarioSenha(session)

    except (NoteFucionarioSenha) : raise

    except Exception as e:
        raise ErroInesperado(e, session)

def alterar_dados_fucionario(id: int, senha: str  | None, nome: str | None, session: Session) -> dict:
    try:
        query = session.query(Funcionario).filter_by(_id = id).first()

        if query:
            if senha != None : query.senha(senha)  
             
            if nome != None: query.nome = nome 

            if nome is None and senha is None: raise RequestInvalida(session)

        else: raise NoteFucionarioSenha(session)

        session.commit()
        return {'mensagem': 'fucionaro editado com sucesso.'}

    except (NoteFucionarioSenha, RequestInvalida) : raise

    except Exception as e:
        raise ErroInesperado(e, session)

def dados_fucionario(id: int, session: Session):
    try:
        query = session.query(Funcionario).filter_by(_id = id).first()

        if query is not None:
            return {
                'mensagem':{
                    'nome' : query.nome,
                    'login' : query.login
                }
            }
        else: raise NoteFucionarioSenha(session)
    
    except (NoteFucionarioSenha): raise

    except Exception as e:
        raise ErroInesperado(e, session) 


