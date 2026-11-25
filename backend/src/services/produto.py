from sqlalchemy.orm import Session
from ..models import Produto, EnumCategoria
from .erros import RequestInvalida, ErroInesperado, NoteProduto


def criar_produto(categoria: EnumCategoria, nome: str, preco: float, desc: str, session: Session) -> dict:
    try:
        produto: Produto
        produto = Produto(categoria, nome, preco, desc)
        session.add(produto)
        session.commit()
        return {'mensagem': 'produto criado com sucesso'}
    except Exception as e:
        raise ErroInesperado(e, session)


def del_produto(id: int, session: Session) -> dict:
    try:
        query = session.query(Produto).filter_by(_id=id).delete()

        if query:
            session.commit()
            return {"mensagem": "produto removido."}
        else:
            raise NoteProduto(session)

    except NoteProduto:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_produto(id: int, categoria: EnumCategoria | None, nome: str | None, preco: float | None, 
                          desc: str | None, session: Session) -> dict:
    try:
        query = session.query(Produto).filter_by(_id=id).first()

        if query:
            if categoria is not None: query.categoria = categoria
            if nome is not None: query._nome = nome
            if preco is not None: query.preco = preco
            if desc is not None: query.desc = desc

            if categoria is None and nome is None and preco is None and desc is None:
                raise RequestInvalida(session)
        else:
            raise NoteProduto(session)

        session.commit()
        return {'mensagem': 'produto editado com sucesso.'}

    except (NoteProduto, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_produto(id: int, session: Session):
    try:
        query = session.query(Produto).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'categoria': query.categoria,
                    'nome': query.nome,
                    'preco': query.preco,
                    'desc': query.desc
                }
            }
        else:
            raise NoteProduto(session)

    except NoteProduto:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
