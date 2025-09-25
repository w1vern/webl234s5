
import os
from uuid import UUID

from dotenv import load_dotenv
from faststream.rabbit import RabbitBroker, RabbitQueue, fastapi
from pydantic import BaseModel

load_dotenv()


RABBIT_USER = os.getenv("RABBIT_USER")
RABBIT_PASSWORD = os.getenv("RABBIT_PASSWORD")
RABBIT_IP = os.getenv("RABBIT_IP")
RABBIT_PORT = os.getenv("RABBIT_PORT")

if RABBIT_USER is None or RABBIT_PASSWORD is None or RABBIT_IP is None or RABBIT_PORT is None:
    raise Exception("Environment variables are not set")

RABBIT_URL = f"amqp://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_IP}:{RABBIT_PORT}"

router = fastapi.RabbitRouter(RABBIT_URL)

class RabbitMessage(BaseModel):
    chat_id: UUID
    message: str


rabbit_queue_to_backend = RabbitQueue(name="backend")
rabbit_queue_to_neural = RabbitQueue(name="neural")

def get_broker() -> RabbitBroker:
    return router.broker


async def send_message(broker: RabbitBroker, queue: RabbitQueue | str, data: RabbitMessage | dict):
    await broker.publish(data, queue)
