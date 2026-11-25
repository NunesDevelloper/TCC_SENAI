from sqlalchemy.orm import Session
from ..models import Estoque, Fornecedor
from .erros import ErroInesperado,EstoqueJaPossuiFornecedor,FornecedorPossuiEstoque,NoteEstoque,NoteFornecedor,RequestInvalida

def associar_fornecedor_estoque(fornecedor_id: int,estoque_id: int,session: Session,) -> dict:
    try:
        query_f = session.query(Fornecedor).filter_by(_id=fornecedor_id).first()
        if query_f is None:
            raise NoteFornecedor(session)

        query_e = session.query(Estoque).filter_by(_id=estoque_id).with_for_update().first()

        if query_e is None:
            raise NoteEstoque(session)

        if query_e.fornecedores:
            raise EstoqueJaPossuiFornecedor(session)

        query_e.fornecedores.append(query_f)
        session.commit()
        return {"mensagem": "fornecedor associado ao ingrediente com sucesso"}
    except (EstoqueJaPossuiFornecedor,NoteEstoque,NoteFornecedor):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def criar_fornecedor(cnpj: str, nome: str, contato: str, session: Session) -> dict:
    try:
        fornecedor: Fornecedor
        fornecedor = Fornecedor(cnpj, nome, contato)
        session.add(fornecedor)
        session.commit()
        return {'mensagem': 'fornecedor criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_fornecedor(id: int, session: Session) -> dict:
    try:
        query = session.query(Fornecedor).filter_by(_id=id).first()
        if query is None:
            raise NoteFornecedor(session)
        if query.estoques:
            raise FornecedorPossuiEstoque(session)

        session.delete(query)
        session.commit()
        return {"mensagem": "fornecedor removido."}

    except (FornecedorPossuiEstoque, NoteFornecedor):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_fornecedor(id: int, cnpj: str | None, nome: str | None,
                             contato: str | None, session: Session) -> dict:
    try:
        query = session.query(Fornecedor).filter_by(_id=id).first()

        if query:
            if cnpj is not None: query.cnpj = cnpj
            if nome is not None: query.nome = nome
            if contato is not None: query.contato = contato

            if cnpj is None and nome is None and contato is None:
                raise RequestInvalida(session)
        else:
            raise NoteFornecedor(session)

        session.commit()
        return {'mensagem': 'fornecedor editado com sucesso.'}

    except (NoteFornecedor, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_fornecedor(id: int, session: Session):
    try:
        query = session.query(Fornecedor).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'cnpj': query.cnpj,
                    'nome': query.nome,
                    'contato': query.contato
                }
            }
        else:
            raise NoteFornecedor(session)

    except NoteFornecedor:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def listar_fornecedores(session: Session) -> dict:
    try:
        fornecedores = session.query(Fornecedor).order_by(Fornecedor._id).all()
        return {
            "mensagem": [
                {
                    "id": fornecedor.id,
                    "cnpj": fornecedor.cnpj,
                    "nome": fornecedor.nome,
                    "contato": fornecedor.contato,
                }
                for fornecedor in fornecedores
            ]
        }
    except Exception as e:
        raise ErroInesperado(e, session)
