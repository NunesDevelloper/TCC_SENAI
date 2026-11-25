from sqlalchemy.orm import Session
from ..models import HistoricoPedidos
from .erros import RequestInvalida, ErroInesperado, NoteHistoricoPedidos


def criar_historico_pedidos(carrinho_id: int, session: Session,status: str = 'preparo') -> dict:
    try:
        historico: HistoricoPedidos
        historico = HistoricoPedidos(carrinho_id, status)
        session.add(historico)
        session.commit()
        return {'mensagem': 'histórico de pedidos criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_historico_pedidos(id: int, session: Session) -> dict:
    try:
        query = session.query(HistoricoPedidos).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "histórico de pedidos removido."}
        else:
            raise NoteHistoricoPedidos(session)

    except NoteHistoricoPedidos:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_historico_pedidos(id: int, carrinho_id: int | None,status: str | None, session: Session) -> dict:
    try:
        query = session.query(HistoricoPedidos).filter_by(_id=id).first()

        if query:
            if carrinho_id is not None: query._carrinho_id = carrinho_id
            if status is not None: query.status = status

            if carrinho_id is None and status is None:
                raise RequestInvalida(session)
        else:
            raise NoteHistoricoPedidos(session)

        session.commit()
        return {'mensagem': 'histórico de pedidos editado com sucesso.'}

    except (NoteHistoricoPedidos, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_historico_pedidos(id: int, session: Session):
    try:
        query = session.query(HistoricoPedidos).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'carrinho_id': query.carrinho_id,
                    'status': query.status
                }
            }
        else:
            raise NoteHistoricoPedidos(session)

    except NoteHistoricoPedidos:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
