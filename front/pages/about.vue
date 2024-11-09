<script setup>
import { ref, computed } from 'vue';

const cards = ref([
    { label: 'Профессионализм и надежность', text: 'Наша юридическая компания специализируется на предоставлении полного спектра правовых услуг для бизнеса и частных клиентов. Мы оказываем поддержку в сложных правовых вопросах, консультируем и защищаем интересы наших клиентов на каждом этапе сотрудничества.' },
    { label: 'Команда экспертов', text: 'В команде — опытные юристы и адвокаты, обладающие глубокими знаниями в различных отраслях права, от корпоративного и налогового до семейного и наследственного права. Мы верим в индивидуальный подход и стремимся найти лучшее решение для каждой ситуации, основываясь на многолетнем опыте и актуальных правовых знаниях.' },
    { label: 'Наши ценности', text: 'Ответственность, честность и уважение к клиенту — это принципы, на которых строится наша работа. Мы уверены, что открытое общение и соблюдение профессиональной этики являются основой долгосрочных и доверительных отношений.' },
    { label: 'Ваши права — наша миссия', text: 'Наша компания объединяет лучших специалистов для решения любых юридических вопросов. Мы оказываем комплексные правовые услуги, помогаем клиентам справляться с кризисными ситуациями и обеспечиваем надежную правовую поддержку в делах любой сложности.' },
    { label: 'Комплексный подход', text: 'Мы предлагаем комплексный подход к каждому делу, разрабатываем стратегии и находим уникальные решения, которые отвечают нуждам наших клиентов. Независимо от сложности вопроса, мы обеспечиваем внимательное и персонализированное обслуживание для достижения результата.' },
    { label: 'Наши гарантии', text: 'Мы гарантируем профессионализм, четкость и ответственность в каждом нашем действии. Работаем с полной вовлеченностью, соблюдая все обязательства перед клиентом. Нам доверяют, и это доверие — основа нашей репутации.' }
]);

const currentIndex = ref(0);

const currentCard = computed(() => cards.value[currentIndex.value]);

function nextCard() {
    currentIndex.value = (currentIndex.value + 1) % cards.value.length;
}

function prevCard() {
    currentIndex.value = (currentIndex.value - 1 + cards.value.length) % cards.value.length;
}
</script>

<template>
    <div class="page">
        <Header></Header>
        <div class="content_with_footer">
            <div class="content">
                <div class="carousel">
                    <button @click="prevCard" class="carousel-button">◀</button>
                    <div class="card">
                        <p class="label">{{ currentCard.label }}</p>
                        <p class="text">{{ currentCard.text }}</p>
                    </div>
                    <button @click="nextCard" class="carousel-button">▶</button>
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
    margin-top: 8rem;
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}

.carousel {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.card {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 30vw;
    padding: 2rem;
    background-color: var(--p-surface-100);
    border-radius: 1rem;
    gap: 1rem;
}

.label {
    font-size: 2rem;
}

.text {
    font-size: 1.5rem;
}

.carousel-button {
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: var(--primary-color, #000);
    padding: 1rem;
}
</style>
