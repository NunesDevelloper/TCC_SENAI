import redis
from ..config import DB_PASSWORD, DB_IP

redis_conection = redis.Redis(
    host=DB_IP, 
    port=6379, 
    password=DB_PASSWORD,
    decode_responses=True
)
