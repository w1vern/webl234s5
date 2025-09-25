import { definePreset } from "@primevue/themes";
import Aura from "@primevue/themes/aura"
import 'dotenv/config'
require("dotenv").config()


const surface = {
  50 : '{zinc.50}',
  100: '{zinc.100}',
  200: '{zinc.200}',
  300: '{zinc.300}',
  400: '{zinc.400}',
  500: '{zinc.500}',
  600: '{zinc.600}',
  700: '{zinc.700}',
  800: '{zinc.800}',
  900: '{zinc.900}',
  950: '{zinc.950}'
}

const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{red.50}',
      100: '{red.100}',
      200: '{red.200}',
      300: '{red.300}',
      400: '{red.400}',
      500: '{red.500}',
      600: '{red.600}',
      700: '{red.700}',
      800: '{red.800}',
      900: '{red.900}',
      950: '{red.950}'
    },
    colorScheme: {
      light: {
        surface: surface
      },
      dark: {
        surface: surface
      }
    }
  }
});

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  runtimeConfig: {
    public: {
      yandexToken: process.env.NUXT_PUBLIC_YANDEX_TOKEN || process.env.YANDEX_TOKEN || '',
      apiBase: '/'
    },
  },
  nitro: {
    devProxy: {
      '/api': {
        target: `http://localhost:8000/api`,
        changeOrigin: true,
        ws: true,
      }
    }
  },
  devServer: {
    host: "0.0.0.0",
    port: 3000
  },
  compatibilityDate: '2024-04-03',
  devtools: {
    enabled: true,

    timeline: {
      enabled: true
    }
  },
  modules: [
    '@primevue/nuxt-module',
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
  css: [
    'primeicons/primeicons.css'
  ]
})