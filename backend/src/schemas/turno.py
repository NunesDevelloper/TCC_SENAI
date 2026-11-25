from datetime import datetime
from pydantic import BaseModel
from ..models import EnumCargo


class BaseCriarTurno(BaseModel):
    cargo: EnumCargo
    funcionario_id: int
    dt_final: datetime | None = None
    dt_inicio: datetime | None = None


class BaseEditarTurno(BaseModel):
    cargo: EnumCargo | None = None
    funcionario_id: int | None = None
    dt_inicio: datetime | None = None
    dt_final: datetime | None = None


class ResponseDadosTurno(BaseModel):
    class DicReponse(BaseModel):
        cargo: str
        funcionario_id: int
        dt_inicio: datetime
        dt_final: datetime | None

    mensagem: DicReponse
