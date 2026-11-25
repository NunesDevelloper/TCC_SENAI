from sqlalchemy.orm import Session
from ..models import Estoque, EnumUnidadeMedida, Fornecedor
from .erros import ErroInesperado,EstoquePossuiFornecedor,EstoqueUsadoEmProduto,NoteEstoque,NoteFornecedor,RequestInvalida


def criar_estoque(item_nome: str, preco_uni: float, quantidade: str, fornecedor_id: int, session: Session,
                  unidade_medida: EnumUnidadeMedida = EnumUnidadeMedida.Uni) -> dict:
    try:
        query_f = session.query(Fornecedor).filter_by(_id=fornecedor_id).first()
        if query_f is None:
            raise NoteFornecedor(session)

        estoque = Estoque(item_nome, preco_uni, quantidade, unidade_medida)
        estoque.fornecedores.append(query_f)
        session.add(estoque)
        session.commit()
        return {'mensagem': 'estoque criado com sucesso'}
    except NoteFornecedor:
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def del_estoque(id: int, session: Session) -> dict:
    try:
        query = session.query(Estoque).filter_by(_id=id).first()
        if query is None:
            raise NoteEstoque(session)
        if query.produtos:
            raise EstoqueUsadoEmProduto(session)
        if query.fornecedores:
            raise EstoquePossuiFornecedor(session)

        session.delete(query)
        session.commit()
        return {"mensagem": "estoque removido."}

    except (EstoquePossuiFornecedor, EstoqueUsadoEmProduto, NoteEstoque):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_estoque(id: int, item_nome: str | None, preco_uni: float | None,
                          quantidade: str | None, unidade_medida: EnumUnidadeMedida | None,session: Session) -> dict:
    try:
        query = session.query(Estoque).filter_by(_id=id).first()

        if query:
            if item_nome is not None: query.item_nome = item_nome
            if preco_uni is not None: query.preco_uni = preco_uni
            if quantidade is not None: query.quantidade = quantidade
            if unidade_medida is not None: query.unidade_medida = unidade_medida

            if (item_nome is None and preco_uni is None and quantidade is None
                    and unidade_medida is None):
                raise RequestInvalida(session)
        else:
            raise NoteEstoque(session)

        session.commit()
        return {'mensagem': 'estoque editado com sucesso.'}

    except (NoteEstoque, RequestInvalida):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def dados_estoque(id: int, session: Session):
    try:
        query = session.query(Estoque).filter_by(_id=id).first()

        if query is not None:
            return {
                'mensagem': {
                    'item_nome': query.item_nome,
                    'preco_uni': query.preco_uni,
                    'quantidade': query.quantidade,
                    'unidade_medida': query.unidade_medida
                }
            }
        else:
            raise NoteEstoque(session)

    except NoteEstoque:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
