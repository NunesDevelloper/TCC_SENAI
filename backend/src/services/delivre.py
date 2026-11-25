from sqlalchemy.orm import Session
from ..models import Carrinho, Delivre
from .erros import DelivreComPedidos,ErroInesperado,NoteCarrinho,NoteDelivre,PedidoJaTemEntregador,PedidoNaoEhDelivery,RequestInvalida



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
        query = session.query(Delivre).filter_by(_id=id).first()
        if query is None:
            raise NoteDelivre(session)
        if query.carrinhos:
            raise DelivreComPedidos(session)

        session.delete(query)
        session.commit()
        return {"mensagem": "delivre removido."}

    except (DelivreComPedidos, NoteDelivre):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def associar_pedido_delivre(delivre_id: int, carrinho_id: int, session: Session) -> dict:
    try:
        query_d = session.query(Delivre).filter_by(_id=delivre_id).first()
        if query_d is None:
            raise NoteDelivre(session)

        query_c = session.query(Carrinho).filter_by(_id=carrinho_id).with_for_update().first()

        if query_c is None:
            raise NoteCarrinho(session)

        if not query_c.is_delivre:
            raise PedidoNaoEhDelivery(session)
        if query_c.deliveries:
            raise PedidoJaTemEntregador(session)

        query_d.carrinhos.append(query_c)
        session.commit()
        return {"mensagem": "entregador atribuído ao pedido com sucesso"}
    except (
        NoteCarrinho,
        NoteDelivre,
        PedidoJaTemEntregador,
        PedidoNaoEhDelivery,
    ):
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


def listar_delivres(session: Session) -> dict:
    try:
        delivres = session.query(Delivre).order_by(Delivre._id).all()
        return {
            "mensagem": [
                {"id": delivre._id, "nome": delivre._nome}
                for delivre in delivres
            ]
        }
    except Exception as e:
        raise ErroInesperado(e, session)
