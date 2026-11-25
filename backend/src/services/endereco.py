from sqlalchemy.orm import Session
from ..models import Cliente, Endereco
from .erros import ErroInesperado, NoteEndereco, NoteUserSenha, RequestInvalida


def criar_endereco(logradouro: str, bairro: str, cep: str, cliente_id: int,
                   session: Session, numero: int | None = None,
                   complemento: str | None = None) -> dict:
    try:
        cliente = session.query(Cliente).filter_by(_id=cliente_id).first()
        if cliente is None:
            raise NoteUserSenha(session)

        endereco: Endereco
        endereco = Endereco(logradouro, bairro, cep, numero, complemento)
        cliente.enderecos.append(endereco)
        session.add(endereco)
        session.commit()
        return {'mensagem': 'endereço criado com sucesso'}
    except NoteUserSenha:
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def del_endereco(id: int, cliente_id: int, session: Session) -> dict:
    try:
        cliente = session.query(Cliente).filter_by(_id=cliente_id).first()
        if cliente is None:
            raise NoteUserSenha(session)

        query = session.query(Endereco).join(Endereco.clientes).filter(Endereco._id == id, Cliente._id == cliente_id).first()

        if query is None:
            raise NoteEndereco(session)

        cliente.enderecos.remove(query)
        if not query.clientes:
            session.delete(query)
        session.commit()
        return {"mensagem": "endereço removido."}
    except (NoteEndereco, NoteUserSenha):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def alterar_dados_endereco(id: int, logradouro: str | None, bairro: str | None, cep: str | None, numero: int | None,complemento: str | None, 
                           cliente_id: int,session: Session) -> dict:
    try:
        query = session.query(Endereco).join(Endereco.clientes).filter(Endereco._id == id, Cliente._id == cliente_id).first()
        

        if query:
            if logradouro is not None: query.logradouro = logradouro
            if bairro is not None: query.bairro = bairro
            if cep is not None: query.cep = cep
            if numero is not None: query.numero = numero
            if complemento is not None: query.complemento = complemento

            if (logradouro is None and bairro is None and cep is None
                    and numero is None and complemento is None):
                raise RequestInvalida(session)
        else:
            raise NoteEndereco(session)

        session.commit()
        return {'mensagem': 'endereço editado com sucesso.'}

    except (NoteEndereco, RequestInvalida):
        raise
    except Exception as e:
        raise ErroInesperado(e, session)


def dados_endereco(id: int, cliente_id: int, session: Session):
    try:
        query = session.query(Endereco).join(Endereco.clientes).filter(Endereco._id == id, Cliente._id == cliente_id).first()

        if query is not None:
            return {
                'mensagem': {
                    'logradouro': query.logradouro,
                    'numero': query.numero,
                    'complemento': query.complemento,
                    'bairro': query.bairro,
                    'cep': query.cep
                }
            }
        else:
            raise NoteEndereco(session)

    except NoteEndereco:
        raise

    except Exception as e:
        raise ErroInesperado(e, session)
