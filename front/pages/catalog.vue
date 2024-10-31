<script setup>

import InputText from 'primevue/inputtext';

const in_search = ref('')

const cards = ref([

    {
        label: 'Ликвидация',
        description: 'Добровольная официальная ликвидация — единственный законный способ прекращения деятельности юридического лица. Компания может быть ликвидирована, только решив все свои проблемы с кредиторами и отчетностью.',
        price: 'от 40000р',
        picture: '/img/store1.jpg'
    },
    {
        label: 'Реорганизация',
        description: 'Реорганизация – процедура реформирования бизнеса с передачей прав и обязанностей правопреемнику – другому юридическому лицу: слияние, присоединение, выделение, разделение, преобразование и сочетания таких форм.',
        price: 'от 35000р',
        picture: '/img/reorganization.webp'
    },
    {
        label: 'Банкротство',
        description: 'Банкротство – это единственный законный способ ликвидации предприятия с долгами. Это сложная и специфическая процедура. Зачастую, есть много факторов, которые усложняют процесс. Поэтому, стоимость услуги нужно обсуждать индивидуально.',
        price: 'Рассчитывается индивидуально',
        picture: '/img/default.jpg'
    },
    {
        label: 'Ведение дел в судах',
        description: 'Представительство на стороне истца, ответчика, третьего лица, участие на всех стадиях процесса. Мы берем ход дела под свой контроль и помогаем добиться исполнения решения суда.',
        price: 'от 30000р',
        picture: '/img/store2.jpg'
    },
    {
        label: 'Юридические консультации',
        description: 'Оперативные устные консультации, составление правовых заключений, экспертное мнение адвоката.',
        price: 'от 1000р',
        picture: '/img/store5.jpg'
    },
    {
        label: 'Составление договоров',
        description: 'Разработка договоров, контрактов, подготовка правовой документации, заявлений, жалоб, претензий и т.п.',
        price: 'от 5000р',
        picture: '/img/store6.webp'
    },
])

const filtered = computed(() => {
    let search = in_search.value.toLowerCase()
    return cards.value.filter(card =>
        card.label.toLowerCase().includes(search) ||
        card.description.toLowerCase().includes(search) ||
        card.price.toLowerCase().includes(search)
    )

})



</script>

<template>
    <div class="page">

        <Header></Header>
        <div class="content_with_footer">
            <div class="content">
                <div class="menu">
                    <div class="search">
                        <InputText class="search_field" type="text" v-model="in_search"
                            placeholder="Введите поисковый запрос"></InputText>
                    </div>
                    <div class="catalog">
                        <div class="catalog_card" v-for="card in filtered">
                            <div class="text_fields">
                                <p class="label">
                                    Услуга: {{ card.label }}
                                </p>
                                <p class="text">
                                    Описание: {{ card.description }}
                                </p>
                                <p class="price">
                                    Цена: {{ card.price }}
                                </p>
                            </div>
                            <img :src="card.picture" alt="picture" class="picture">
                        </div>
                    </div>
                </div>

            </div>
            <Footer></Footer>
        </div>
    </div>
</template>

<style scoped>
.page {
    min-height: 100vh;
}

.content_with_footer {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.content {
    margin-top: 5rem;
    flex-grow: 1;
}

.menu {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-content: center;
    align-items: center;
    gap: 2rem;
    padding: 4rem;
}

.search_field {
    width: 30rem;
    height: 2.5rem;
    font-size: 1.5rem;
}

.catalog {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 5rem;
}

.catalog_card {
    display: flex;
    flex-direction: row;
    padding: 2rem;
    background-color: var(--p-surface-100);
    border-radius: 1rem;
    gap:2rem;
}

.text_fields {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.label {
    font-size: 2rem;
}

.text {
    font-size: 1.5rem;
}

.price {

    font-size: 1.5rem;
}

.picture {
    border-radius: 1rem;
    width: 40%;
    height: max-content;

}
</style>