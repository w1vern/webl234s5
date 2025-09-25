
from fastapi import Depends
from redis.asyncio import Redis

from database.rabbit import RabbitMessage, rabbit_queue_to_backend, router
from database.redis import RedisDB, get_redis_client


@router.subscriber(rabbit_queue_to_backend)
async def handler(message: RabbitMessage, redis: Redis = Depends(get_redis_client)) -> None:
    await redis.set(f"{RedisDB.ws_answers.value}:{message.chat_id}", message.message)