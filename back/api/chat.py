
import asyncio
from uuid import UUID

from fastapi import APIRouter, Depends, WebSocket
from faststream.rabbit import RabbitBroker
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from back.authorize_user import authorize_user
from back.schemes.chat import Chat, Message
from database.database import session_manager
from database.models.user import User
from database.rabbit import (RabbitMessage, get_broker, rabbit_queue_to_neural,
                             send_message)
from database.redis import RedisDB, get_redis_client
from database.repositories.chat_repository import ChatRepository
from database.repositories.message_repository import MessageRepository

router = APIRouter(prefix='/chat', tags=['chat'])


@router.websocket('/ws/{chat_id}')
async def websocket_endpoint(websocket: WebSocket,
                             chat_id: UUID,
                             broker: RabbitBroker = Depends(get_broker),
                             redis: Redis = Depends(get_redis_client),
                             ) -> None:
    print("Websocket connected")
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await send_message(broker, rabbit_queue_to_neural, RabbitMessage(chat_id=chat_id, message=data))
            ans = await redis.get(f"{RedisDB.ws_answers.value}:{chat_id}")
            if not ans is None:
                await websocket.send_text(ans)
                await redis.delete(f"{RedisDB.ws_answers.value}:{chat_id}")
            await asyncio.sleep(0.5)
    except Exception as e:
        print(e)
    finally:
        print("Websocket disconnected")
        await websocket.close()


@router.post('')
async def create(session: AsyncSession = Depends(session_manager.session),
                 user: User = Depends(authorize_user)
                 ) -> Chat:
    cr = ChatRepository(session)
    chat = await cr.create(name="Chat", user=user)
    return Chat(id=chat.id, name=chat.name)


@router.get('/{chat_id}/messages')
async def get_messages(chat_id: UUID,
                       session: AsyncSession = Depends(
                           session_manager.session),
                       user: User = Depends(authorize_user)
                       ) -> list[Message]:
    mr = MessageRepository(session)
    cr = ChatRepository(session)
    chat = await cr.get_by_id(id=chat_id)
    if chat is None:
        return []
    messages = await mr.get_by_chat(chat=chat)
    return [Message(text=message.text, from_user=message.from_user) for message in messages]


@router.get('')
async def get_all(session: AsyncSession = Depends(session_manager.session),
                  user: User = Depends(authorize_user)
                  ) -> list[Chat]:
    cr = ChatRepository(session)
    chats = await cr.get_by_user(user=user)
    return [Chat(id=chat.id, name=chat.name) for chat in chats]
