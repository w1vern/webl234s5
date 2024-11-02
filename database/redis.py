

import redis
import redis.client

def get_redis_client() -> redis.client.Redis:
    return redis.Redis(host='localhost', port=6379, db=0)

