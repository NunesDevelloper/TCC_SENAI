from fastapi import HTTPException, status
from sqlalchemy.orm import Session

#region user
class DuplicationUser(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='já existe um cliente com esse email'
        )

class NoteUserSenha(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há User Verificado com esse Email"
        )
#endregion

#region fucionario
class DuplicationFucionario(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='já existe um fucioanrio com esse login'
        )

class NoteFucionarioSenha(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há fucionario com esse login"
        )
#endregion

#region carrinho
class NoteCarrinho(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há carrinho com esse id"
        )

class FormaPedidoInvalida(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O pedido não pode ser delivery e retirada ao mesmo tempo"
        )

class AtendenteSemTurnoAtivo(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O funcionário precisa estar em um turno ativo como atendente para receber pedidos"
        )

class CupomForaValidade(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O cupom de desconto está fora da validade"
        )

class CupomJaUtilizado(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Esse cliente já utilizou o cupom de desconto"
        )

class PedidoNaoPodeSerExcluido(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Pedidos não podem ser excluídos; registre o cancelamento no histórico de status"
        )

class ClientePedidoObrigatorio(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O cliente do pedido é obrigatório"
        )

class AtendentePedidoObrigatorio(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O atendente do pedido é obrigatório"
        )

class ClienteNaoPodeAlterarResponsaveisPedido(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="O cliente não pode alterar o cliente ou atendente do pedido"
        )

#endregion

#region combo
class NoteCombo(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há combo com esse id"
        )

class PrecoComboNegativo(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O preço do combo não pode ser negativo"
        )
#endregion

#region cumpom_desconto
class NoteCupomDesconto(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há cupom de desconto com esse id"
        )

class PercentualCupomInvalido(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O percentual de desconto deve ser maior que zero e menor ou igual a 100"
        )

class ValidadeCupomInvalida(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="A validade do cupom deve estar no futuro"
        )
#endregion

#region delivre
class NoteDelivre(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há delivre com esse id"
        )

class PedidoNaoEhDelivery(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Só é possível atribuir um entregador a pedidos de delivery"
        )

class PedidoJaTemEntregador(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O pedido já possui um entregador responsável"
        )

class PedidoComEntregadorNaoPodeMudarTipo(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não é possível alterar a modalidade de um pedido com entregador atribuído"
        )

class DelivreComPedidos(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não é possível remover um entregador que possui pedidos atribuídos"
        )

#endregion

#region endereco
class NoteEndereco(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há endereço com esse id"
        )
#endregion

#region estoque
class NoteEstoque(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há estoque com esse id"
        )

class IngredienteJaVinculado(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Esse ingrediente já está vinculado ao produto"
        )

class EstoqueUsadoEmProduto(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não é possível remover um ingrediente usado por produtos"
        )

class EstoquePossuiFornecedor(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não é possível remover um ingrediente com fornecedor associado"
        )
#endregion

#region fornecedor
class NoteFornecedor(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há fornecedor com esse id"
        )

class EstoqueJaPossuiFornecedor(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O ingrediente já possui um fornecedor responsável"
        )

class FornecedorPossuiEstoque(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não é possível remover um fornecedor associado a ingredientes"
        )

#endregion

#region historico_pedidos
class NoteHistoricoPedidos(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há histórico de pedidos com esse id"
        )

class HistoricoPedidoImutavel(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O histórico de status é permanente; registre uma nova mudança de status"
        )
#endregion

#region mesa
class NoteMesa(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há mesa com esse id"
        )
#endregion

#region produto
class NoteProduto(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há produto com esse id"
        )

class ProdutoSemIngredientes(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O produto deve possuir ao menos um ingrediente"
        )

class IngredientesRepetidos(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="A lista de ingredientes não pode conter ids repetidos"
        )

class ProdutoPossuiIngredientes(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não é possível remover um produto que possui ingredientes associados"
        )

class PrecoProdutoNegativo(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O preço do produto não pode ser negativo"
        )
#endregion

#region turno
class NoteTurno(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há turno com esse id"
        )

class PeriodoTurnoInvalido(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="O término do turno deve ser posterior ao início"
        )
#endregion

#region geral
class ErroInesperado(HTTPException):
    def __init__(self, e, session: Session | None = None):
        if session is not None:
            session.rollback()

        super().__init__(
            status_code=500,
            detail=f"Erro inesperado do servidor.Erro -> {e}"
        )

class DnsEmailNotExiste(HTTPException):
    def __init__(self):

        super().__init__(
            status_code=422,
            detail= "Dns do email não existe"
        )


class RequestInvalida(HTTPException):
    def __init__(self, session: Session | None = None):
        
        if session is not None: session.rollback()

        super().__init__(
            status_code=422,
            detail= "Nem um campo devidamente informado"
        )

class JwtInvalido(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )

class JwtNotEmail(HTTPException):
    def __init__(self, session: Session):
        session.rollback()
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de redefinição inválido ou já utilizado"
        )

class FuncioanroAllow(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso permitido somente para clientes"
        )

class JustFucioanrio(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso permitido somente para funcionários"
        )

class AutStmpServer(HTTPException):
    def __init__(self, session: Session):
        session.rollback()
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Falha na autenticação do servidor de e-mail"
        )

class StmpIndisponivel(HTTPException):
    def __init__(self, session: Session):
        session.rollback()
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Servidor de e-mail indisponível"
        )
#endregion

    