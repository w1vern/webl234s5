



import asyncio
from database.database import sessionmanager
from database.repositories.product_repository import ProductRepository

catalog = [

    {
        "label": 'Ликвидация',
        "description": 'Добровольная официальная ликвидация — единственный законный способ прекращения деятельности юридического лица. Компания может быть ликвидирована, только решив все свои проблемы с кредиторами и отчетностью.',
        "price": 'от 40000р',
        "picture": '/img/store1.jpg',
        "worker_count": 4
    },
    {
        "label": 'Реорганизация',
        "description": 'Реорганизация – процедура реформирования бизнеса с передачей прав и обязанностей правопреемнику – другому юридическому лицу: слияние, присоединение, выделение, разделение, преобразование и сочетания таких форм.',
        "price": 'от 35000р',
        "picture": '/img/reorganization.webp',
        "worker_count": 3
    },
    {
        "label": 'Банкротство',
        "description": 'Банкротство – это единственный законный способ ликвидации предприятия с долгами. Это сложная и специфическая процедура. Зачастую, есть много факторов, которые усложняют процесс. Поэтому, стоимость услуги нужно обсуждать индивидуально.',
        "price": 'Рассчитывается индивидуально',
        "picture": '/img/default.jpg',
        "worker_count": 5
    },
    {
        "label": 'Ведение дел в судах',
        "description": 'Представительство на стороне истца, ответчика, третьего лица, участие на всех стадиях процесса. Мы берем ход дела под свой контроль и помогаем добиться исполнения решения суда.',
        "price": 'от 30000р',
        "picture": '/img/store2.jpg',
        "worker_count": 2
    },
    {
        "label": 'Юридические консультации',
        "description": 'Оперативные устные консультации, составление правовых заключений, экспертное мнение адвоката.',
        "price": 'от 1000р',
        "picture": '/img/store5.jpg',
        "worker_count": 1
    },
    {
        "label": 'Составление договоров',
        "description": 'Разработка договоров, контрактов, подготовка правовой документации, заявлений, жалоб, претензий и т.п.',
        "price": 'от 5000р',
        "picture": '/img/store6.webp',
        "worker_count": 1
    },
]


async def main():
    async with sessionmanager.session() as session:
        pr = ProductRepository(session)
        for product in catalog:
            await pr.create(label=product['label'], description=product['description'], price=product['price'], path_to_image=product['picture'], worker_count=product['worker_count'])

        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())