from sqlalchemy.orm import Session
from ..models import Estoque, EnumCategoria, Produto
from .erros import ErroInesperado,IngredientesRepetidos,IngredienteJaVinculado,NoteEstoque,NoteProduto,PrecoProdutoNegativo,ProdutoSemIngredientes,ProdutoPossuiIngredientes,RequestInvalida

def associar_ingrediente_produto(produto_id: int,estoque_id: int,session: Session,) -> dict:
    try:
        query = session.query(Produto).filter_by(_id=produto_id).with_for_update().first()

        if query is None:
            raise NoteProduto(session)
        produto = query

        query = session.query(Estoque).filter_by(_id=estoque_id).first()
        if query is None:
            raise NoteEstoque(session)
        ingrediente = query

        if ingrediente in produto.estoques:
            raise IngredienteJaVinculado(session)

        produto.estoques.append(ingrediente)
        session.commit()
        return {"mensagem": "ingrediente associado ao produto com sucesso"}
    except (IngredienteJaVinculado, NoteEstoque,NoteProduto,):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def criar_produto(categoria: EnumCategoria,nome: str,preco: float,
                  desc: str,estoque_ids: list[int],session: Session,) -> dict:
    try:
        if preco < 0:
            raise PrecoProdutoNegativo(session)
        if not estoque_ids:
            raise ProdutoSemIngredientes(session)
        if len(estoque_ids) != len(set(estoque_ids)):
            raise IngredientesRepetidos(session)

        query = session.query(Estoque).filter(Estoque._id.in_(estoque_ids)).with_for_update().all()

        if len(query) != len(estoque_ids):
            raise NoteEstoque(session)

        produto = Produto(categoria, nome, preco, desc)
        produto.estoques.extend(query)
        session.add(produto)
        session.commit()
        return {'mensagem': 'produto criado com sucesso'}
    except (IngredientesRepetidos,NoteEstoque,PrecoProdutoNegativo,ProdutoSemIngredientes,):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def del_produto(id: int, session: Session) -> dict:
    try:
        query = session.query(Produto).filter_by(_id=id).first()
        if query is None:
            raise NoteProduto(session)
        if query.estoques:
            raise ProdutoPossuiIngredientes(session)

        session.delete(query)
        session.commit()
        return {"mensagem": "produto removido."}

    except (NoteProduto, ProdutoPossuiIngredientes):
        raise

    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_produto(id: int, categoria: EnumCategoria | None, nome: str | None, preco: float | None, 
                          desc: str | None, session: Session) -> dict:
    try:
        query = session.query(Produto).filter_by(_id=id).first()

        if query:
            if preco is not None and preco < 0:
                raise PrecoProdutoNegativo(session)
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

    except (NoteProduto, PrecoProdutoNegativo, RequestInvalida):
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
