

from enum import Enum
import redis
import redis.client

class RedisDB(str, Enum):
    basket = "basket"
    process = "process"
    auth_session = "auth_session"


def get_redis_client() -> redis.client.Redis:
    return redis.Redis(host='localhost', port=6379, db=0)

