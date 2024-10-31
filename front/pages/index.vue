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
            text: "Мы оказываем полное сопровождение бизнеса, начиная с консультаций по регистрации компании, реорганизации и ликвидации, заканчивая решениями корпоративных споров и ведением документации. Наши специалисты готовы помочь вам с составлением учредительных документов, оптимизацией структуры управления и соблюдением всех законодательных требований, чтобы обеспечить бесперебойную деятельность компании.",
            button_label: "В каталог",
            picture_path: "img/index-1.webp",
            alt_picture: "index-1"

        },
        left:
        {
            label: "Защита прав работников и работодателей",
            text: "Мы предлагаем комплексную поддержку в решении трудовых вопросов, начиная с разработки и адаптации трудовых договоров, отвечающих требованиям законодательства и потребностям компании. Наши специалисты консультируют по вопросам правовых гарантий и обязательств работников и работодателей, обеспечивая соблюдение интересов обеих сторон.",
            button_label: "В каталог",
            picture_path: "img/index-2.webp",
            alt_picture: "index-2"
        }
    },
    {
        right: {
            label: "Эффективное налоговое планирование",
            text: "Мы предоставляем комплексные консультации по вопросам налогообложения, помогая вам снизить налоговую нагрузку и минимизировать риски. Наши эксперты анализируют специфику вашей деятельности, выявляют налоговые льготы и разрабатывают индивидуальные решения для оптимизации налоговых выплат, полностью соответствующие законодательству.",
            button_label: "В каталог",
            picture_path: "img/index-3.webp",
            alt_picture: "index-3"

        },
        left:
        {
            label: "Альтернативное разрешение споров",
            text: "Мы предлагаем профессиональные услуги по разрешению споров вне суда, используя методы переговоров, медиации и других альтернативных подходов для достижения взаимовыгодных решений. Наши специалисты помогают сторонам в конструктивном обсуждении вопросов, минимизируя конфликтность и снижая финансовые и временные затраты, связанные с судебными разбирательствами.",
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
    background-color: var(--p-surface-200);
    color: var(--p-surface-950)
}

.commercial {
    display: flex;
    width: 100%;
    gap: 2rem;
    padding: 5rem;
}

.left_commercial {
    background-color: var(--p-surface-300)
}

.picture {
    width: 50%;
    height: max-content;
    padding: 6rem;
    border-radius: 7rem;
}

.card_text {
    padding: 6rem;
    width: 50%;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    font-size: 1.5rem;
}
.label {
    font-size: 2.5rem;
}
.text {
    font-size: 1.8rem
}

.button {
    width: 8rem;
    font-size: 1.5rem;
}
</style>