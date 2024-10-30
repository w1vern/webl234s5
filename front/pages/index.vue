<script setup>

import Button from 'primevue/button';

const router = useRouter()

async function to_catalog() {
    router.push('/catalog')
}

const commercial_cards = ref([
    {
        right: {
            label: "Поддержка бизнеса на всех этапах",
            text: "Консультируем по вопросам регистрации, реорганизации и ликвидации компаний, корпоративным спорам и ведению документации.",
            button_label: "В каталог",
            picture_path: "img/index-1.webp",
            alt_picture: "index-1"

        },
        left:
        {
            label: "Защита прав работников и работодателей",
            text: "Помогаем решать трудовые конфликты, разрабатывать трудовые договоры и регулировать трудовые отношения.",
            button_label: "В каталог",
            picture_path: "img/index-2.webp",
            alt_picture: "index-2"
        }
    },
    {
        right: {
            label: "Эффективное налоговое планирование",
            text: "Консультируем по вопросам налогообложения, помогаем минимизировать налоговые риски и оптимизировать выплаты.",
            button_label: "В каталог",
            picture_path: "img/index-3.webp",
            alt_picture: "index-3"

        },
        left:
        {
            label: "Альтернативное разрешение споров",
            text: "Предоставляем услуги по разрешению споров вне суда, через переговоры и медиацию.",
            button_label: "В каталог",
            picture_path: "img/index-4.webp",
            alt_picture: "index-4"
        }
    }
])


</script>

<template>
    <div class="page">

        <Header></Header>
        <div class="content_with_footer">
            <div class="content">
                <div class="base_info">

                </div>
                <div class="cards">
                    <div class="card" v-for="(commercial_card, index) in commercial_cards" :key="index">
                        <div class="commercial right_commercial">
                            <div class="card_text">
                                <p class="label">
                                    {{ commercial_card.right.label }}
                                </p>
                                <p class="text">
                                    {{ commercial_card.right.text }}
                                </p>
                                <Button class="button" :label="commercial_card.right.button_label"
                                    @click="to_catalog"></Button>
                            </div>
                            <img class="picture" :src="commercial_card.right.picture_path"
                                :alt="commercial_card.right.alt_picture">
                        </div>
                        <div class="commercial left_commercial">
                            <img class="picture" :src="commercial_card.left.picture_path"
                                :alt="commercial_card.left.alt_picture">
                            <div class="card_text">
                                <p class="label">
                                    {{ commercial_card.left.label }}
                                </p>
                                <p class="text">
                                    {{ commercial_card.left.text }}
                                </p>
                                <Button class="button" :label="commercial_card.left.button_label"
                                    @click="to_catalog"></Button>
                            </div>
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
    padding-top: 5rem;
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.content {
    flex-grow: 1;
    background-color: var(--p-surface-800);
    color: var(--p-surface-50)
}

.commercial {
    display: flex;
    width: 100%;
    gap: 2rem;
    padding: 5rem;
}

.left_commercial {
    background-color: var(--p-surface-600)
}

.picture {
    width: 50%;
    padding: 3rem;
}

.card_text {
    width: 50%;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    font-size: 1.5rem;
}

.button {
    width: 8rem;
}
</style>