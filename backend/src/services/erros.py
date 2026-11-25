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
#endregion

#region combo
class NoteCombo(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há combo com esse id"
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
#endregion

#region delivre
class NoteDelivre(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há delivre com esse id"
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
#endregion

#region fornecedor
class NoteFornecedor(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há fornecedor com esse id"
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
#endregion

#region turno
class NoteTurno(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há turno com esse id"
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
#endregion

    