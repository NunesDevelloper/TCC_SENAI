from sqlalchemy.orm import Session
from datetime import datetime
from ..models import Turno, EnumCargo
from .erros import RequestInvalida, ErroInesperado, NoteTurno


def criar_turno(cargo: EnumCargo, funcionario_id: int, session: Session,
                dt_final: datetime | None = None,
                dt_inicio: datetime | None = None) -> dict:
    try:
        turno: Turno
        turno = Turno(cargo, dt_final, dt_inicio or datetime.now())
        turno.funcionario_id = funcionario_id
        session.add(turno)
        session.commit()
        return {'mensagem': 'turno criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_turno(id: int, session: Session) -> dict:
    try:
        query = session.query(Turno).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "turno removido."}
        else:
            raise NoteTurno(session)

    except NoteTurno:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_turno(id: int, cargo: EnumCargo | None, funcionario_id: int | None, 
            dt_inicio: datetime | None, dt_final: datetime | None, session: Session) -> dict:
    try:
        query = session.query(Turno).filter_by(_id=id).first()

        if query:
            if cargo is not None: query.cargo = cargo
            if funcionario_id is not None: query.funcionario_id = funcionario_id
            if dt_inicio is not None: query._dt_inicio = dt_inicio
            if dt_final is not None: query._dt_final = dt_final

            if (cargo is None and funcionario_id is None and dt_inicio is None
                    and dt_final is None):
                raise RequestInvalida(session)
        else:
            raise NoteTurno(session)

        session.commit()
        return {'mensagem': 'turno editado com sucesso.'}

    except (NoteTurno, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_turno(id: int, session: Session):
    try:
        query = session.query(Turno).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'cargo': query.cargo,
                    'funcionario_id': query.funcionario_id,
                    'dt_inicio': query._dt_inicio,
                    'dt_final': query._dt_final
                }
            }
        else:
            raise NoteTurno(session)

    except NoteTurno:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
