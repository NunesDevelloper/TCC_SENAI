import redis
from ..config import DB_PASSWORD

redis_conection = redis.Redis(
    host='redis', 
    port=6379, 
    password=DB_PASSWORD,
    decode_responses=True
)
