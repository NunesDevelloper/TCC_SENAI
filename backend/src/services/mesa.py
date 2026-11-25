from sqlalchemy.orm import Session
from ..models import Mesa
from .erros import RequestInvalida, ErroInesperado, NoteMesa


def criar_mesa(numero: int, session: Session) -> dict:
    try:
        mesa: Mesa
        mesa = Mesa(numero)
        session.add(mesa)
        session.commit()
        return {'mensagem': 'mesa criada com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_mesa(id: int, session: Session) -> dict:
    try:
        query = session.query(Mesa).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "mesa removida."}
        else:
            raise NoteMesa(session)

    except NoteMesa:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_mesa(id: int, numero: int | None, session: Session) -> dict:
    try:
        query = session.query(Mesa).filter_by(_id=id).first()

        if query:
            if numero is not None: query._numero = numero

            if numero is None:
                raise RequestInvalida(session)
        else:
            raise NoteMesa(session)

        session.commit()
        return {'mensagem': 'mesa editada com sucesso.'}

    except (NoteMesa, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_mesa(id: int, session: Session):
    try:
        query = session.query(Mesa).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'numero': query.numero
                }
            }
        else:
            raise NoteMesa(session)

    except NoteMesa:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
