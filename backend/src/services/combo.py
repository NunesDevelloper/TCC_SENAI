from sqlalchemy.orm import Session
from ..models import Combo
from .erros import RequestInvalida, ErroInesperado, NoteCombo


def criar_combo(nome: str, preco: float, session: Session, desc: str | None = None) -> dict:
    try:
        combo: Combo
        combo = Combo(nome, preco, desc)
        session.add(combo)
        session.commit()
        return {'mensagem': 'combo criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_combo(id: int, session: Session) -> dict:
    try:
        query = session.query(Combo).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "combo removido."}
        else:
            raise NoteCombo(session)

    except NoteCombo:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_combo(id: int, nome: str | None, preco: float | None, desc: str | None, session: Session) -> dict:
    try:
        query = session.query(Combo).filter_by(_id=id).first()

        if query:
            if nome is not None: query._nome = nome
            if preco is not None: query._preco = preco
            if desc is not None: query._desc = desc

            if nome is None and preco is None and desc is None:
                raise RequestInvalida(session)
        else:
            raise NoteCombo(session)

        session.commit()
        return {'mensagem': 'combo editado com sucesso.'}

    except (NoteCombo, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_combo(id: int, session: Session):
    try:
        query = session.query(Combo).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'nome': query._nome,
                    'preco': query._preco,
                    'desc': query._desc
                }
            }
        else:
            raise NoteCombo(session)

    except NoteCombo:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
