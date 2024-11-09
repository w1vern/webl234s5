<script setup>

import InputText from 'primevue/inputtext';

const in_search = ref('')

const catalog_store = useCatalogStore()
const basket_store = useBasketStore()

await callOnce(catalog_store.fetch)
await callOnce(basket_store.fetch_state)

const filtered = computed(() => {
    let search = in_search.value.toLowerCase()
    return catalog_store.catalog.filter(card =>
        card.label.toLowerCase().includes(search) ||
        card.description.toLowerCase().includes(search) ||
        card.price.toLowerCase().includes(search)
    )
})

definePageMeta({
  title: 'Каталог',
  need_auth: true
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
                                    Цена: {{ card.price }} ₽
                                </p>
                                <Button class="add_to_basket" @click="basket_store.add_product(card.id)">
                                    Добавить в корзину
                                </Button>
                                <p class="count">
                                    Осталось: {{ card.can_be_ordered }}
                                </p>
                            </div>
                            <img :src="card.path_to_image" alt="picture" class="picture">
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

.count {
    font-size: 1rem;
}
</style>