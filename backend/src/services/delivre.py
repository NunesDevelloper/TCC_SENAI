from sqlalchemy.orm import Session
from ..models import Delivre
from .erros import RequestInvalida, ErroInesperado, NoteDelivre


def criar_delivre(nome: str | None, session: Session) -> dict:
    try:
        delivre: Delivre
        delivre = Delivre(nome)
        session.add(delivre)
        session.commit()
        return {'mensagem': 'delivre criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_delivre(id: int, session: Session) -> dict:
    try:
        query = session.query(Delivre).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "delivre removido."}
        else:
            raise NoteDelivre(session)

    except NoteDelivre:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_delivre(id: int, nome: str | None, session: Session) -> dict:
    try:
        query = session.query(Delivre).filter_by(_id=id).first()

        if query:
            if nome is not None: query.nome = nome

            if nome is None:
                raise RequestInvalida(session)
        else:
            raise NoteDelivre(session)

        session.commit()
        return {'mensagem': 'delivre editado com sucesso.'}

    except (NoteDelivre, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_delivre(id: int, session: Session):
    try:
        query = session.query(Delivre).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'nome': query._nome
                }
            }
        else:
            raise NoteDelivre(session)

    except NoteDelivre:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
