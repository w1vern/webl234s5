<script setup>

import { ref } from 'vue'
import { useRouter } from 'vue-router'

import Button from 'primevue/button';

const router = useRouter()

async function to_catalog() {
    router.push('/catalog')
}

const commertial_cards = ref([
    {
        right: {
            label: "Мы поможем вам",
            text: "Предлагаем корпоративным клиентам и частным лицам услуги в области правового и финансового консалтинга: юридические услуги, бухгалтерские услуги, регистрация и ликвидация фирм, регистрация оффшоров, а также услуги в сфере международного налогового планирования",
            button_label: "В каталог",
            picture_path: "img/first_index_picture.png",
            alt_picture: "first_index_picture"

        },
        left:
        {
            label: "Быстро и удобно",
            text: `<br>
				Откройте бизнес "под ключ"<br>
				<ul type="circle">
					<li> Сбор информации об организации
					<li> Подписание и подача документов
					<li> Получение документов
				</ul>
				<br>
				Бухгалтерские услуги<br>
				<ol type="a">
					<li> Абонентское бухгалтерское обслуживание
					<li> Нулевая отчетность
					<li> Восстановление бухгалтерского учета
				</ol>`,
            button_label: "В каталог",
            picture_path: "img/second_index_picture.png",
            alt_picture: "second_index_picture"
        }
    },
    {
        right: {
            label: "В любой точке Земного шара",
            text: `<ol type="A">
					<li>Международное налоговое планирование и консалтинг
					</li>
					<li> Оффшоры. Регистрация компаний за рубежом
						<ol type="a">
							<li> Сейшелы
							</li>
							<li> Британские Виргинские Острова
							</li>
						</ol>
					<li> Контролируемые иностранные компании
				</ol>`,
            button_label: "В каталог",
            picture_path: "img/third_index_picture.png",
            alt_picture: "third_index_picture"

        },
        left:
        {
            label: "Услуги высшего качества",
            text: "Юридические консультации, ведение дел в судах, все виды юридических услуг. Обширный профессиональный опыт наших адвокатов обеспечит качественную защиту Ваших интересов. Интересы клиента и его доверие — наш приоритет. Вся информация, которую Вы доверяете своему адвокату, является адвокатской тайной и охраняется законом.",
            button_label: "В каталог",
            picture_path: "img/fourth_index_picture.png",
            alt_picture: "fourth_index_picture"
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
                    <div class="card" v-for="(commertial_card, index) in commertial_cards" :key="index">
                        <div class="right_commertial">
                            <img class="picture" :src="commertial_card.right.picture_path"
                                :alt="commertial_card.right.alt_picture">
                            <div class="card_text">
                                <p class="label">
                                    {{ commertial_card.right.label }}
                                </p>
                                <p class="text">
                                    {{ commertial_card.right.text }}
                                </p>
                                <Button class="button" :label="commertial_card.right.button_label" @click="to_catalog"></Button>
                            </div>
                        </div>
                        <div class="left_commertial">
                            <img class="picture" :src="commertial_card.left.picture_path"
                                :alt="commertial_card.left.alt_picture">
                            <div class="card_text">
                                <p class="label">
                                    {{ commertial_card.left.label }}
                                </p>
                                <p class="text">
                                    {{ commertial_card.left.text }}
                                </p>
                                <Button class="button" :label="commertial_card.left.button_label" @click="to_catalog"></Button>
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
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.content {
    flex-grow: 1;
    background-color: var(--p-surface-950);
    color: var(--p-surface-50)
}
</style>