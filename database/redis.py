

from enum import Enum
import redis
import redis.client

class RedisDB(str, Enum):
    basket = "basket"
    auth_session = "auth_session"
    free_workers = "free_workers"


def get_redis_client() -> redis.Redis:
    return redis.Redis(host='localhost', port=6379, db=0)

