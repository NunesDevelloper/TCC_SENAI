from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import jwt, JWTError
from datetime import datetime, timezone
from ..models import EnumCargo
from uuid import uuid4
from .erros import ErroInesperado, JwtInvalido, FuncioanroAllow, JustFucioanrio
from ..config import SECRETES_KEY,ALG,TIMER

oauth_schema = OAuth2PasswordBearer('/auth/login_conta')

def criar_token(id_user: int, fucionario: EnumCargo= None,  is_fucioanrio : bool= False) -> str:
    try:
        dt_expi = datetime.now(timezone.utc) + TIMER

        dic_info = None

        dic_info = {'sub': str(id_user),'exp': dt_expi,  
                    "is_fucionario" : is_fucioanrio,}
        
        #Cria o JWT
        jwt_codificado = jwt.encode(dic_info, SECRETES_KEY, ALG)#type: ignore
        return jwt_codificado
    
    except Exception as e:
        raise ErroInesperado(e)

def criar_token_email(id_user: int) -> str:
    try:
        dt_expi = datetime.now(timezone.utc) + TIMER

        dic_info = None

        dic_info = {'sub': str(id_user),'exp': dt_expi,  
                    "jit": str(uuid4())}
        
        #Cria o JWT
        jwt_codificado = jwt.encode(dic_info, SECRETES_KEY, ALG)#type: ignore
        return jwt_codificado
    
    except Exception as e:
        raise ErroInesperado(e)

def verificar_jwt(token: str) -> tuple:
    try:
        dict_info = jwt.decode(token, str(SECRETES_KEY), str(ALG))
        id = int(dict_info['sub'])

        if "jit" in dict_info.keys():
            jit = str(dict_info["jit"])

            return id, jit

        is_fucionario = bool(dict_info['is_fucionario'])

        return id, is_fucionario
    
    except JWTError:
        raise JwtInvalido()
    
    except Exception as e:
        raise ErroInesperado(e)

def verificar_jwt_user(token = Depends(oauth_schema)) -> int:
    try:
        id, is_fucionario = verificar_jwt(token)
        
        if is_fucionario == True: raise FuncioanroAllow()

        return int(id)

    except (JwtInvalido, FuncioanroAllow): raise
    
    except Exception as e: raise ErroInesperado(e)

def verificar_jwt_fucionario(token = Depends(oauth_schema)) -> int:
    try:
        id, is_fucionario = verificar_jwt(token)
        
        if is_fucionario == False: raise JustFucioanrio()

        return int(id)
    
    except (JwtInvalido, JustFucioanrio): raise

    except Exception as e: raise ErroInesperado(e)