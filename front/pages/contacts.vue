<script setup>
import { YandexMap, YandexMapDefaultFeaturesLayer, YandexMapDefaultMarker, YandexMapDefaultSchemeLayer } from 'vue-yandex-maps';
import IftaLabel from 'primevue/iftalabel';
import Textarea from 'primevue/textarea';

const map = shallowRef(null);

const contacts = ref([
  {
    title: "Офис в Москве",
    address: "Москва, ул. Красная Пресня, д. 24, Бизнес-центр «Сибирь», 1-й вход, 3 этаж",
    phones: ["8 (800) 555-83-25", "+7 (495) 966-15-56"],
    working_time: "пн‑пт: 10:00‑19:00",
    image: "/img/office1.jpg",
    coordinates: [55.762277, 37.569899]
  },
  {
    title: "Офис в Санкт-Петербурге",
    address: "Санкт-Петербург, ул. Большая Конюшенная, д. 29, Бизнес-центр «Эра-Хаус», 4 этаж",
    phones: ["8 (800) 555-83-25", "+7 (812) 677-26-64"],
    working_time: "пн‑пт: 10:00‑19:00",
    image: "/img/office2.jpg",
    coordinates: [59.936688, 30.322102]
  }
])

const markers = computed(() => {
  let new_markers = []
  for (let i = 0; i < contacts.value.length; i++) {
    const element = contacts.value[i];
    let new_coords = [element.coordinates[1], element.coordinates[0]]
    new_markers.push({
      coordinates: new_coords,
      color: "#ea580c",
      title: element.title
    })
  }
  return new_markers
})

const form_data = ref({ name: "", email: "", message: "" })

async function send_form() {

}

</script>

<template>
  <div class="page">

    <Header></Header>
    <div class="content_with_footer">
      <div class="content">
        <div class="overlay">
          <div class="offices">
            <template v-for="office in contacts">
              <Office :office="office"></Office>
            </template>
          </div>
        </div>
        <div class="map">
          <YandexMap v-model="map" :settings="{
            location: {
              center: [35.520673, 58.277288],
              zoom: 6,
            },
          }" width="100%" height="100%">
            <YandexMapDefaultSchemeLayer />
            <YandexMapDefaultFeaturesLayer />
            <YandexMapDefaultMarker v-for="(marker, ind) in markers" :settings="marker" :key="ind">
            </YandexMapDefaultMarker>
          </YandexMap>
        </div>
        <div class="feedback">
          <div class="feedback_form">
            <div class="form_header">
              <div class="name">
                <IftaLabel>
                  <InputText id="username" v-model="form_data.name" pt:root="input_inside"/>
                  <label for="username"> Ваше имя</label>
                </IftaLabel>
              </div>
              <div class="email">
                <IftaLabel>
                  <InputText id="email" v-model="form_data.email" pt:root="input_inside"/>
                  <label for="email"> Электронная почта</label>
                </IftaLabel>
              </div>
            </div>
            <div class="form_text">
              <Textarea v-model="form_data.message" autoResize rows="5" cols="55" placeholder="Расскажите о своей проблеме" pt:root="input_inside"/>
            </div>
            <Button class="form_button" label="Отправить" @click="send_form"></Button>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </div>
</template>

<style scoped>

.input_inside {
 width: 100%;
 min-width: 0;
}

.overlay {
  background-color: rgba(255, 255, 255, 0.8);
  position: absolute;
  top: 7.5rem;
  left: 1rem;
  width: max-content;
  height: max-content;
  z-index: 999;
}

.offices {
  padding: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.page {
  min-height: 100vh;
}

.content_with_footer {
  display: flex;
  flex-direction: column;

  min-height: 100vh;
}

.content {
  display: flex;
  flex-direction: column;
}

.map {
  height: 90vh;
}

.feedback {
  display: flex;
  height: max-content;
  flex-grow: 1;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  align-content: center;
  margin-top: 5rem;
  margin-bottom: 5rem;
}

.feedback_form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  padding: 2rem;
  gap: 1.5rem;
  background-color: var(--p-surface-100);
  border-radius: 0.5rem;
  width: 40rem;
}

.form_header {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 1rem;

}

.name {
  flex-grow: 1;
}

.email {
  flex-grow: 1;
}

.form_text {
  width: 100%;
}

.form_button {
  width: 100%;
}
</style>