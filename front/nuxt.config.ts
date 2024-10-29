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
    },
    surface: {
      50: '{neutral.950}',
      100: '{neutral.100}',
      200: '{neutral.200}',
      300: '{neutral.300}',
      400: '{neutral.400}',
      500: '{neutral.500}',
      600: '{neutral.600}',
      700: '{neutral.700}',
      800: '{neutral.800}',
      900: '{neutral.900}',
      950: '{neutral.50}'
    }
  }
});

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    host: "0.0.0.0",
    port: 3000
  },
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: [
    '@primevue/nuxt-module',
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