from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_sesion
from ..schemas import BaseCriarCupomDesconto, BaseEditarCupomDesconto, ResponseDadosCupomDesconto, ResponseOk
from ..services import alterar_dados_cupom_desconto,criar_cupom_desconto,dados_cupom_desconto,del_cupom_desconto,verificar_jwt_fucionario

Rotas_CupomDesconto = APIRouter(
    responses={
        404: {"description": "Não há cupom de desconto com esse id"},
        401: {"description": "Não autorizado"}
    }
)


@Rotas_CupomDesconto.post("/criar_cupom_desconto",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)],)
async def criar_CupomDesconto(base: BaseCriarCupomDesconto, session: Session = Depends(get_sesion)):
    return criar_cupom_desconto(base.id, base.codigo, base.percentual_desconto, base.dt_valida, session)


@Rotas_CupomDesconto.get("/", response_model=ResponseDadosCupomDesconto)
async def dados_CupomDesconto(id: int, session: Session = Depends(get_sesion)):
    return dados_cupom_desconto(id, session)


@Rotas_CupomDesconto.delete("/",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)],)
async def deletar_CupomDesconto(id: int, session: Session = Depends(get_sesion)):
    return del_cupom_desconto(id, session)


@Rotas_CupomDesconto.put("/Editar_CupomDesconto",response_model=ResponseOk,dependencies=[Depends(verificar_jwt_fucionario)],)
async def editar_CupomDesconto(base: BaseEditarCupomDesconto, id: int, session: Session = Depends(get_sesion)):
    return alterar_dados_cupom_desconto(id, base.codigo, base.percentual_desconto, base.dt_valida, session)
