from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session, selectinload
from ..models import Carrinho,CupomDesconto,EnumCargo,EnumMetedoPagamento,Turno
from .erros import AtendentePedidoObrigatorio,AtendenteSemTurnoAtivo,ClienteNaoPodeAlterarResponsaveisPedido,ClientePedidoObrigatorio,CupomForaValidade,CupomJaUtilizado,ErroInesperado,FormaPedidoInvalida,NoteCarrinho,NoteCupomDesconto,PedidoComEntregadorNaoPodeMudarTipo,PedidoNaoPodeSerExcluido,RequestInvalida

def _validar_forma_entrega(is_delivre: bool,is_retirada: bool,session: Session,) -> None:
    if is_delivre and is_retirada:
        raise FormaPedidoInvalida(session)


def _validar_atendente(funcionario_id: int, session: Session) -> None:
    agora = datetime.now()
    query = session.query(Turno).filter(
        Turno.funcionario_id == funcionario_id,
        Turno._cargo == EnumCargo.atendente,
        Turno._dt_inicio <= agora).first()

    if query is None:
        raise AtendenteSemTurnoAtivo(session)


def _validar_cupom(cliente_id: int,cupom_desconto_id: int,session: Session,pedido_id: int | None = None) -> None:
    query = session.query(CupomDesconto).filter_by(_id=cupom_desconto_id).with_for_update().first()
    if query is None:
        raise NoteCupomDesconto(session)

    validade = query.dt_valida
    agora = datetime.now()
    if validade <= agora:
        raise CupomForaValidade(session)

    query = session.query(Carrinho).filter(
        Carrinho._cliente_id == cliente_id,
        Carrinho._cupom_desconto_id == cupom_desconto_id)
    if pedido_id is not None:
        query = query.filter(Carrinho._id != pedido_id)
    if query.first() is not None:
        raise CupomJaUtilizado(session)


def _definir_responsaveis(cliente_id: int | None,funcionario_id: int | None,identidade: tuple[int, bool],
                          session: Session) -> tuple[int, int]:
    usuario_id, is_funcionario = identidade
    if is_funcionario:
        if cliente_id is None:
            raise ClientePedidoObrigatorio(session)
        return cliente_id, usuario_id

    if funcionario_id is None:
        raise AtendentePedidoObrigatorio(session)
    return usuario_id, funcionario_id


def criar_carrinho(cliente_id: int | None,funcionario_id: int | None,mesa_id: int,cupom_desconto_id: int,session: 
                   Session,identidade: tuple[int, bool],is_delivre: bool = False,is_retirada: bool = False,
                   metedo_pagamento: EnumMetedoPagamento = EnumMetedoPagamento.pix) -> dict:
    try:
        cliente_id, funcionario_id = _definir_responsaveis(
            cliente_id, funcionario_id, identidade, session
        )
        _validar_forma_entrega(is_delivre, is_retirada, session)
        _validar_atendente(funcionario_id, session)
        _validar_cupom(cliente_id, cupom_desconto_id, session)

        carrinho = Carrinho(cliente_id,funcionario_id,mesa_id,cupom_desconto_id,is_delivre,is_retirada,metedo_pagamento)
        session.add(carrinho)
        session.commit()
        return {"mensagem": "carrinho criado com sucesso"}
    except (AtendentePedidoObrigatorio,AtendenteSemTurnoAtivo,ClientePedidoObrigatorio,
            CupomForaValidade,CupomJaUtilizado,FormaPedidoInvalida,NoteCupomDesconto):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def del_carrinho(id: int,session: Session,identidade: tuple[int, bool]) -> dict:
    try:
        query = session.query(Carrinho).filter_by(_id=id)
        usuario_id, is_funcionario = identidade
        if not is_funcionario:
            query = query.filter_by(_cliente_id=usuario_id)
        query = query.first()
        if query is None:
            raise NoteCarrinho(session)
        raise PedidoNaoPodeSerExcluido(session)
    except (NoteCarrinho, PedidoNaoPodeSerExcluido):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_carrinho(id: int,session: Session,identidade: tuple[int, bool],
                           cliente_id: int | None = None,funcionario_id: int | None = None,
                           mesa_id: int | None = None,cupom_desconto_id: int | None = None,is_delivre: bool | None = None,
                           is_retirada: bool | None = None,metedo_pagamento: EnumMetedoPagamento | None = None,) -> dict:
    try:
        usuario_id, is_funcionario = identidade
        if not is_funcionario and (cliente_id is not None or funcionario_id is not None):
            raise ClienteNaoPodeAlterarResponsaveisPedido(session)

        query = session.query(Carrinho).filter_by(_id=id)
        if not is_funcionario:
            query = query.filter_by(_cliente_id=usuario_id)
        query = query.first()
        if query is None:
            raise NoteCarrinho(session)

        nova_entrega = is_delivre if is_delivre is not None else query._is_delivre
        nova_retirada = is_retirada if is_retirada is not None else query._is_retirada
        _validar_forma_entrega(nova_entrega, nova_retirada, session)
        if not nova_entrega and query.deliveries:
            raise PedidoComEntregadorNaoPodeMudarTipo(session)

        if funcionario_id is not None:
            _validar_atendente(funcionario_id, session)

        novo_cliente_id = cliente_id if cliente_id is not None else query._cliente_id
        novo_cupom_id = (
            cupom_desconto_id
            if cupom_desconto_id is not None
            else query._cupom_desconto_id
        )
        if cliente_id is not None or cupom_desconto_id is not None:
            _validar_cupom(novo_cliente_id, novo_cupom_id, session, id)

        if all(
            value is None
            for value in (
                cliente_id,
                funcionario_id,
                mesa_id,
                cupom_desconto_id,
                is_delivre,
                is_retirada,
                metedo_pagamento,
            )
        ):
            raise RequestInvalida(session)

        if cliente_id is not None:
            query._cliente_id = cliente_id
        if funcionario_id is not None:
            query._funcionario_id = funcionario_id
        if mesa_id is not None:
            query._mesa_id = mesa_id
        if cupom_desconto_id is not None:
            query._cupom_desconto_id = cupom_desconto_id
        if is_delivre is not None:
            query._is_delivre = is_delivre
        if is_retirada is not None:
            query._is_retirada = is_retirada
        if metedo_pagamento is not None:
            query._metedo_pagamento = metedo_pagamento

        session.commit()
        return {"mensagem": "carrinho editado com sucesso."}
    except (AtendenteSemTurnoAtivo,ClienteNaoPodeAlterarResponsaveisPedido,CupomForaValidade,
            CupomJaUtilizado,FormaPedidoInvalida,NoteCarrinho,NoteCupomDesconto,
            PedidoComEntregadorNaoPodeMudarTipo,RequestInvalida,):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def dados_carrinho(id: int,session: Session,identidade: tuple[int, bool]) -> dict:
    try:
        query = session.query(Carrinho).filter_by(_id=id)
        usuario_id, is_funcionario = identidade
        if not is_funcionario:
            query = query.filter_by(_cliente_id=usuario_id)
        query = query.first()
        if query is None:
            raise NoteCarrinho(session)

        return {
            "mensagem": {
                "cliente_id": query._cliente_id,
                "funcionario_id": query._funcionario_id,
                "mesa_id": query._mesa_id,
                "cupom_desconto_id": query._cupom_desconto_id,
                "is_delivre": query._is_delivre,
                "is_retirada": query._is_retirada,
                "metedo_pagamento": query._metedo_pagamento,
            }
        }
    except NoteCarrinho:
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def historico_pedidos_cliente(cliente_id: int, session: Session) -> dict:
    try:
        query = (
            session.query(Carrinho)
            .options(selectinload(Carrinho.historico))
            .filter(Carrinho._cliente_id == cliente_id)
            .order_by(Carrinho._id.desc())
            .all()
        )

        pedidos = []
        for carrinho in query:
            historico = sorted(carrinho.historico, key=lambda evento: evento._id)
            pedidos.append(
                {
                    "id": carrinho.id,
                    "funcionario_id": carrinho._funcionario_id,
                    "cupom_desconto_id": carrinho._cupom_desconto_id,
                    "is_delivre": carrinho.is_delivre,
                    "is_retirada": carrinho.is_retirada,
                    "mesa_id": carrinho._mesa_id,
                    "metedo_pagamento": carrinho._metedo_pagamento,
                    "status": [
                        evento._status.value
                        if hasattr(evento._status, "value")
                        else str(evento._status)
                        for evento in historico
                    ],
                }
            )

        return {"pedidos": pedidos}
    except Exception as e:
        raise ErroInesperado(e, session)
