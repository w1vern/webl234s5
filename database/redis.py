

import redis
import redis.client

async def get_redis_client() -> redis.client.Redis:
    return await redis.Redis(host='localhost', port=6379, db=0)
