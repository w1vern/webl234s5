import { definePreset } from "@primevue/themes";
import Aura from "@primevue/themes/aura"


const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{orange.50}',
      100: '{orange.100}',
      200: '{orange.200}',
      300: '{orange.300}',
      400: '{orange.400}',
      500: '{orange.500}',
      600: '{orange.600}',
      700: '{orange.700}',
      800: '{orange.800}',
      900: '{orange.900}',
      950: '{orange.950}'
    }
  }
});

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: [
    '@primevue/nuxt-module',
    '@nuxtjs/tailwindcss',
    '@vueuse/nuxt',
    'vue-yandex-maps/nuxt',
    '@pinia/nuxt'
  ],
  primevue: {
    options: {
      theme: {
        preset: MyPreset,
        options: {
          darkModeSelector: false || 'none'
        }
      }
    }
  },
  yandexMaps: {
    apikey: '9088ad51-a476-489c-9d43-c123560ceae9',
  },
  css: [
    'primeicons/primeicons.css'
  ],
  runtimeConfig: {
    public: {
      baseURL: 'http://localhost:8000',
    },
  }
})