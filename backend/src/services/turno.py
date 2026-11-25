from sqlalchemy.orm import Session
from datetime import datetime
from ..models import Turno, EnumCargo
from .erros import ErroInesperado, NoteTurno, PeriodoTurnoInvalido, RequestInvalida

def _validar_periodo(dt_inicio: datetime, dt_final: datetime | None, session: Session) -> None:
    if dt_final is not None and dt_final <= dt_inicio:
        raise PeriodoTurnoInvalido(session)


def criar_turno(cargo: EnumCargo, funcionario_id: int, session: Session,
                dt_final: datetime | None = None,
                dt_inicio: datetime | None = None) -> dict:
    try:
        inicio = dt_inicio or datetime.now()
        _validar_periodo(inicio, dt_final, session)
        turno: Turno
        turno = Turno(cargo, dt_final, inicio)
        turno.funcionario_id = funcionario_id
        session.add(turno)
        session.commit()
        return {'mensagem': 'turno criado com sucesso'}
    except PeriodoTurnoInvalido:
        raise
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
            novo_inicio = dt_inicio if dt_inicio is not None else query._dt_inicio
            novo_final = dt_final if dt_final is not None else query._dt_final
            _validar_periodo(novo_inicio, novo_final, session)

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

    except (NoteTurno, PeriodoTurnoInvalido, RequestInvalida):
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


def listar_turnos(session: Session) -> dict:
    try:
        turnos = session.query(Turno).order_by(Turno._id).all()
        return {
            "mensagem": [
                {
                    "id": turno.id,
                    "cargo": turno._cargo,
                    "funcionario_id": turno.funcionario_id,
                    "dt_inicio": turno._dt_inicio,
                    "dt_final": turno._dt_final,
                }
                for turno in turnos
            ]
        }
    except Exception as e:
        raise ErroInesperado(e, session)
