from sqlalchemy.orm import Session
from ..models import Carrinho, EnumHistorico, HistoricoPedidos
from .erros import ErroInesperado,HistoricoPedidoImutavel,NoteCarrinho,NoteHistoricoPedidos


def criar_historico_pedidos(carrinho_id: int,session: Session,status: EnumHistorico = EnumHistorico.preparo) -> dict:
    try:
        query = session.query(Carrinho).filter_by(_id=carrinho_id).first()
        if query is None:
            raise NoteCarrinho(session)

        historico = HistoricoPedidos(carrinho_id, status)
        session.add(historico)
        session.commit()
        return {"mensagem": "histórico de pedidos criado com sucesso"}
    except NoteCarrinho:
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def del_historico_pedidos(id: int, session: Session) -> dict:
    try:
        query = session.query(HistoricoPedidos).filter_by(_id=id).first()
        if query is None:
            raise NoteHistoricoPedidos(session)
        raise HistoricoPedidoImutavel(session)
    except (HistoricoPedidoImutavel, NoteHistoricoPedidos):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_historico_pedidos(id: int,carrinho_id: int | None,status: EnumHistorico | None,session: Session) -> dict:
    try:
        query = session.query(HistoricoPedidos).filter_by(_id=id).first()
        if query is None:
            raise NoteHistoricoPedidos(session)
        raise HistoricoPedidoImutavel(session)
    except (HistoricoPedidoImutavel, NoteHistoricoPedidos):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def dados_historico_pedidos(id: int, session: Session) -> dict:
    try:
        query = session.query(HistoricoPedidos).filter_by(_id=id).first()
        if query is None:
            raise NoteHistoricoPedidos(session)

        status = query._status
        return {
            "mensagem": {
                "carrinho_id": query.carrinho_id,
                "status": status.value if hasattr(status, "value") else str(status),
            }
        }
    except NoteHistoricoPedidos:
        raise
    except Exception as e:
        raise ErroInesperado(e, session)
