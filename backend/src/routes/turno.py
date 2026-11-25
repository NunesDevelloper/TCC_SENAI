from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarTurno, BaseEditarTurno, ResponseDadosTurno, ResponseOk
from ..services import alterar_dados_turno, criar_turno, dados_turno, del_turno

Rotas_Turno = APIRouter(
    responses={
        404: {"description": "Não há turno com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_Turno.post("/criar_turno", response_model=ResponseOk)
async def criar_Turno(base: BaseCriarTurno, session: Session = Depends(get_sesion)):
    return criar_turno(base.cargo, base.funcionario_id, session, base.dt_final, base.dt_inicio)


@Rotas_Turno.get("/", response_model=ResponseDadosTurno)
async def dados_Turno(id: int, session: Session = Depends(get_sesion)):
    return dados_turno(id, session)


@Rotas_Turno.delete("/", response_model=ResponseOk)
async def deletar_Turno(id: int, session: Session = Depends(get_sesion)):
    return del_turno(id, session)


@Rotas_Turno.put("/Editar_Turno", response_model=ResponseOk)
async def editar_Turno(base: BaseEditarTurno, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_turno(
        id, base.cargo, base.funcionario_id, base.dt_inicio, base.dt_final, session
    )
