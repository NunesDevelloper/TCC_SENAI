from sqlalchemy.orm import Session
from datetime import datetime
from ..models import CupomDesconto
from .erros import RequestInvalida, ErroInesperado, NoteCupomDesconto


def criar_cupom_desconto(id: int, codigo: str, percentual_desconto: float,
                         dt_valida: datetime, session: Session) -> dict:
    try:
        cupom: CupomDesconto
        cupom = CupomDesconto(id, codigo, percentual_desconto, dt_valida)
        session.add(cupom)
        session.commit()
        return {'mensagem': 'cupom de desconto criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_cupom_desconto(id: int, session: Session) -> dict:
    try:
        query = session.query(CupomDesconto).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "cupom de desconto removido."}
        else:
            raise NoteCupomDesconto(session)

    except NoteCupomDesconto:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_cupom_desconto(id: int, codigo: str | None,
  percentual_desconto: float | None, dt_valida: datetime | None, session: Session) -> dict:
    try:
        query = session.query(CupomDesconto).filter_by(_id=id).first()

        if query:
            if codigo is not None: query.codigo = codigo
            if percentual_desconto is not None: query.percentual_desconto = percentual_desconto
            if dt_valida is not None: query.dt_valida = dt_valida

            if codigo is None and percentual_desconto is None and dt_valida is None:
                raise RequestInvalida(session)
        else:
            raise NoteCupomDesconto(session)

        session.commit()
        return {'mensagem': 'cupom de desconto editado com sucesso.'}

    except (NoteCupomDesconto, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_cupom_desconto(id: int, session: Session):
    try:
        query = session.query(CupomDesconto).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'codigo': query.codigo,
                    'percentual_desconto': query.percentual_desconto,
                    'dt_valida': query.dt_valida
                }
            }
        else:
            raise NoteCupomDesconto(session)

    except NoteCupomDesconto:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
