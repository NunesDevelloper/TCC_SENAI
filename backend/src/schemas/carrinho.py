from pydantic import BaseModel
from ..models import EnumMetedoPagamento


class BaseCriarCarrinho(BaseModel):
    cliente_id: int | None = None
    funcionario_id: int | None = None
    mesa_id: int
    cupom_desconto_id: int
    is_delivre: bool = False
    is_retirada: bool = False
    metedo_pagamento: EnumMetedoPagamento = EnumMetedoPagamento.pix


class BaseEditarCarrinho(BaseModel):
    cliente_id: int | None = None
    funcionario_id: int | None = None
    mesa_id: int | None = None
    cupom_desconto_id: int | None = None
    is_delivre: bool | None = None
    is_retirada: bool | None = None
    metedo_pagamento: EnumMetedoPagamento | None = None


class ResponseDadosCarrinho(BaseModel):
    class DicReponse(BaseModel):
        cliente_id: int
        funcionario_id: int
        mesa_id: int
        cupom_desconto_id: int
        is_delivre: bool
        is_retirada: bool
        metedo_pagamento: EnumMetedoPagamento

    mensagem: DicReponse


class ItemHistoricoCliente(BaseModel):
    id: int
    funcionario_id: int
    cupom_desconto_id: int
    is_delivre: bool
    is_retirada: bool
    mesa_id: int
    metedo_pagamento: EnumMetedoPagamento
    status: list[str]


class ResponseHistoricoCliente(BaseModel):
    pedidos: list[ItemHistoricoCliente]
