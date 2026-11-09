from urllib.parse import quote_plus
from dotenv import load_dotenv
from pathlib import Path
from os import getenv

path_env = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(path_env)

class ERRO_ENV(Exception):
    def __init__(self, text: str) -> str:
        print(text)

try:
    DEBUG = getenv("DEBUG")
except(TypeError):
    raise ERRO_ENV("A var \"DEBUG\" não é do tipo booleano.")

#region db
DB_DATABASE = getenv("DB_DATABASE", None)
if DB_DATABASE == None or DB_DATABASE.strip() == " ":
    raise ERRO_ENV("A var \"DB_DATABASE\" não pode está vazia.")

DB_USER = getenv("DB_USER", None)
if DB_USER == None or DB_USER.strip() == " ":
    raise ERRO_ENV("A var \"DB_USER\" não pode está vazia.")

DB_PASSWORD = getenv("DB_PASSWORD", None)
if DB_PASSWORD == None or DB_PASSWORD.strip() == " ":
    raise ERRO_ENV("A var \"DB_PASSWORD\" não pode está vazia.")

DB_PASSWORD = quote_plus(str(getenv("DB_PASSWORD")))

DB_IP = "db"
DB_PORT = 3306

if DEBUG == "True":
    DB_IP = getenv("DB_IP", None)
    if DB_IP == None or DB_IP.strip() == " ":
        raise ERRO_ENV("A var \"DB_IP\" não pode está vazia.")

    try:
        DB_PORT = int(getenv("DB_PORT", 3306))
    except(TypeError):
        raise ERRO_ENV("A var \"DB_PORT\" não é do tipo int.")
#endregion

