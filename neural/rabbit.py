

from faststream import FastStream
from faststream.rabbit import RabbitBroker

from database.database import session_manager
from database.rabbit import (RABBIT_URL, RabbitMessage,
                             rabbit_queue_to_backend, rabbit_queue_to_neural)
from database.repositories.chat_repository import ChatRepository
from database.repositories.message_repository import MessageRepository
from neural.generator import get_answer

broker = RabbitBroker(RABBIT_URL)
app = FastStream(broker)


@broker.subscriber(queue=rabbit_queue_to_neural)
async def handler(message: RabbitMessage) -> None:
    print(f"Message received: {message}")
    async with session_manager.context_session() as session:
        mr = MessageRepository(session)
        cr = ChatRepository(session)
        chat = await cr.get_by_id(message.chat_id)
        if chat is None:
            await broker.publish("Что-то пошло не так", queue=rabbit_queue_to_backend)
            return
        await mr.create(text=message.message, chat=chat, from_user=True)
        await session.commit()
        messages = await mr.get_by_chat(chat)
        answer = await get_answer(messages)
        await mr.create(text=answer, chat=chat, from_user=False)
        message = RabbitMessage(chat_id=message.chat_id, message=answer)
        await broker.publish(message, queue=rabbit_queue_to_backend)
    print(f"Answer sent: {message}")
