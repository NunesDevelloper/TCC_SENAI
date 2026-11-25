from sqlalchemy.orm import Session
from ..models import Carrinho, EnumMetedoPagamento
from .erros import RequestInvalida, ErroInesperado, NoteCarrinho


def criar_carrinho(cliente_id: int, funcionario_id: int, mesa_id: int, cupom_desconto_id: int, session: Session,
                   is_delivre: bool = False, is_retirada: bool = False,
                   metedo_pagamento: EnumMetedoPagamento = EnumMetedoPagamento.pix) -> dict:
    try:
        carrinho: Carrinho
        carrinho = Carrinho(cliente_id, funcionario_id, mesa_id, cupom_desconto_id,is_delivre, 
                            is_retirada, metedo_pagamento)
        session.add(carrinho)
        session.commit()
        return {'mensagem': 'carrinho criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_carrinho(id: int, session: Session) -> dict:
    try:
        query = session.query(Carrinho).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "carrinho removido."}
        else:
            raise NoteCarrinho(session)

    except NoteCarrinho:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_carrinho(id: int, session: Session, cliente_id: int | None = None,
                           funcionario_id: int | None = None, mesa_id: int | None = None,
                           cupom_desconto_id: int | None = None, is_delivre: bool | None = None,
                           is_retirada: bool | None = None,
                           metedo_pagamento: EnumMetedoPagamento | None = None) -> dict:
    try:
        query = session.query(Carrinho).filter_by(_id=id).first()

        if query:
            if cliente_id is not None: query._cliente_id = cliente_id
            if funcionario_id is not None: query._funcionario_id = funcionario_id
            if mesa_id is not None: query._mesa_id = mesa_id
            if cupom_desconto_id is not None: query._cupom_desconto_id = cupom_desconto_id
            if is_delivre is not None: query._is_delivre = is_delivre
            if is_retirada is not None: query._is_retirada = is_retirada
            if metedo_pagamento is not None: query._metedo_pagamento = metedo_pagamento

            if (cliente_id is None and funcionario_id is None and mesa_id is None
                    and cupom_desconto_id is None and is_delivre is None
                    and is_retirada is None and metedo_pagamento is None):
                raise RequestInvalida(session)
        else:
                raise NoteCarrinho(session)

        session.commit()
        return {'mensagem': 'carrinho editado com sucesso.'}

    except (NoteCarrinho, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_carrinho(id: int, session: Session):
    try:
        query = session.query(Carrinho).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'cliente_id': query._cliente_id,
                    'funcionario_id': query._funcionario_id,
                    'mesa_id': query._mesa_id,
                    'cupom_desconto_id': query._cupom_desconto_id,
                    'is_delivre': query._is_delivre,
                    'is_retirada': query._is_retirada,
                    'metedo_pagamento': query._metedo_pagamento
                }
            }
        else:
            raise NoteCarrinho(session)

    except NoteCarrinho:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
