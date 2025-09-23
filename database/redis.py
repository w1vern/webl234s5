

from enum import Enum
from redis.asyncio import Redis
from dotenv import load_dotenv
import os

load_dotenv()
REDIS_IP = os.getenv("REDIS_IP")
REDIS_PORT = os.getenv("REDIS_PORT")

if REDIS_IP is None or REDIS_PORT is None:
    raise Exception("REDIS_IP and REDIS_PORT must be set")


class RedisDB(str, Enum):
    basket = "basket"
    auth_session = "auth_session"
    free_workers = "free_workers"


def get_redis_client() -> Redis:
    return Redis(
        host=REDIS_IP,
        port=int(REDIS_PORT),
        db=0,
        decode_responses=True)
