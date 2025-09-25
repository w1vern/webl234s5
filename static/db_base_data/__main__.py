

import asyncio
import datetime

from back.config import Config
from database.database import session_manager
from database.redis import RedisDB, get_redis_client
from database.repositories.product_repository import ProductRepository

catalog = [

    {
        "label": 'Ликвидация',
        "description": 'Добровольная официальная ликвидация — единственный законный способ прекращения деятельности юридического лица. Компания может быть ликвидирована, только решив все свои проблемы с кредиторами и отчетностью.',
        "price": 40000,
        "sale": 0.05,
        "picture": '/img/store1.jpg',
        "worker_count": 4,
        "time_to_resolve": datetime.timedelta(days=7)
    },
    {
        "label": 'Реорганизация',
        "description": 'Реорганизация – процедура реформирования бизнеса с передачей прав и обязанностей правопреемнику – другому юридическому лицу: слияние, присоединение, выделение, разделение, преобразование и сочетания таких форм.',
        "price": 35000,
        "sale": 0.04,
        "picture": '/img/reorganization.webp',
        "worker_count": 3,
        "time_to_resolve": datetime.timedelta(days=5)
    },
    {
        "label": 'Банкротство',
        "description": 'Банкротство – это единственный законный способ ликвидации предприятия с долгами. Это сложная и специфическая процедура. Зачастую, есть много факторов, которые усложняют процесс. Поэтому, стоимость услуги нужно обсуждать индивидуально.',
        "price": 50000,
        "sale": 0.1,
        "picture": '/img/default.jpg',
        "worker_count": 5,
        "time_to_resolve": datetime.timedelta(days=14)
    },
    {
        "label": 'Ведение дел в судах',
        "description": 'Представительство на стороне истца, ответчика, третьего лица, участие на всех стадиях процесса. Мы берем ход дела под свой контроль и помогаем добиться исполнения решения суда.',
        "price": 30000,
        "sale": 0.04,
        "picture": '/img/store2.jpg',
        "worker_count": 2,
        "time_to_resolve": datetime.timedelta(days=30)
    },
    {
        "label": 'Юридические консультации',
        "description": 'Оперативные устные консультации, составление правовых заключений, экспертное мнение адвоката.',
        "price": 1000,
        "sale": 0.1,
        "picture": '/img/store5.jpg',
        "worker_count": 1,
        "time_to_resolve": datetime.timedelta(hours=1)
    },
    {
        "label": 'Составление договоров',
        "description": 'Разработка договоров, контрактов, подготовка правовой документации, заявлений, жалоб, претензий и т.п.',
        "price": 5000,
        "sale": 0.05,
        "picture": '/img/store6.webp',
        "worker_count": 1,
        "time_to_resolve": datetime.timedelta(days=1)
    },
]


async def main():
	redis = get_redis_client()
	await redis.set(f"{RedisDB.free_workers}", Config.worker_count)
	async with session_manager.context_session() as session:
		pr = ProductRepository(session)
		for product in catalog:
		    await pr.create(label=product['label'],
		                    description=product['description'],
		                    price=product['price'],
		                    sale=product['sale'],
		                    path_to_image=product['picture'],
		                    worker_count=product['worker_count'],
							time_to_resolve=product['time_to_resolve'])


if __name__ == "__main__":
    asyncio.run(main())
