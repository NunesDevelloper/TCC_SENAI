from email_validator import validate_email, EmailNotValidError
import smtplib
from email.message import EmailMessage
from sqlalchemy.orm import Session
from email_validator import validate_email, EmailNotValidError
from ..models import Cliente
from .jwt import criar_token_email, verificar_jwt
from .erros import (NoteUserSenha, AutStmpServer,ErroInesperado,StmpIndisponivel, 
                    JwtNotEmail, JwtInvalido, RequestInvalida)
from ..config import EMAIL_GOOGLE, SENHA_DE_APP, DNS_BASE
from ..db import redis_conection

def is_valido_dns(email:str) -> bool:
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailNotValidError:
        return False


async def enviar_email(email: str, session : Session)-> dict :
    try:
        query = session.query(Cliente).filter_by(_email = email).first()

        if query is None : raise NoteUserSenha(session)

        jwt = criar_token_email(int(query.id))

        url = f"{DNS_BASE}/{jwt}"

        msg = EmailMessage()
        msg['Subject'] = "Resertar senha"
        msg["From"] = EMAIL_GOOGLE
        msg['To'] = query.email

        html =  f"""<!DOCTYPE html>  \n
        <head> \n
            <meta charset="UTF-8">\n
        </head>\n
        <body style="font-family: Arial, sans-serif; padding: 20px; \n
            background: #ffffff,\n
            ; color: #3b82f6; width: 100%; height: 300px;">\n
            <h1>Olá, {query.nome} !</h1>\n
            <p>Aqui está o linck para restar a senha: </p>\n
            <div style="background-color: #ffffffa2; text-align: center; padding:1px ;border-radius: 5px;">\n
                <h3 style="color: #3b82f6; font-size: 24px;">\n
                    <a href="{url} ">click-me</a></h3>\n
            </div>\n
            <p>Esse email foi gerado altomaticamente. Não o responda.\n
                Atenciosamente,\n
            <br>Equipe da cia & lanches</p>\n
        </body>\n
        </html>
        """
       
        msg.set_content(html, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(str(EMAIL_GOOGLE), str(SENHA_DE_APP)) 
            smtp.send_message(msg) 
        
        return{'mensagem':"E-mail enviado"}
    
    except(NoteUserSenha): raise

    except smtplib.SMTPAuthenticationError:
        raise AutStmpServer(session)

    except (smtplib.SMTPServerDisconnected,smtplib.SMTPConnectError):
        raise StmpIndisponivel(session)
    
    except Exception as erro:
        raise ErroInesperado(erro, session) # type: ignore


async def verificar_email_senha(token: str,senha: str ,session: Session)-> dict:
    try:
        id, jit = verificar_jwt(token)

        #ele vai apra blackliste por 5 minutos no redis
        if redis_conection.exists(f"usado:{jit}"): raise JwtNotEmail(session)
        redis_conection.setex(f"usado:{jit}", 900, "true")
       
        query = session.query(Cliente).filter_by(_id = id).first()
        if query is None: raise NoteUserSenha(session)
        query.nova_senha(senha)
        session.commit()   
        return {'mensagem':"Senha Alterada"}
    
    except (JwtNotEmail, NoteUserSenha, JwtInvalido, RequestInvalida): raise 

    except Exception as e: raise ErroInesperado(e, session)


