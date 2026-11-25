from sqlalchemy.orm import Session
from ..models import Fornecedor
from .erros import RequestInvalida, ErroInesperado, NoteFornecedor


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
        query = session.query(Fornecedor).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "fornecedor removido."}
        else:
            raise NoteFornecedor(session)

    except NoteFornecedor:
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
