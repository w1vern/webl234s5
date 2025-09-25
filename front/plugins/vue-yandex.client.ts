// plugins/00-vue-yandex.client.ts
import { defineNuxtPlugin, useRuntimeConfig } from '#app'

export default defineNuxtPlugin(async (nuxtApp) => {
  const config = useRuntimeConfig()
  const apiKey = config.public?.yandexToken || config.public?.NUXT_PUBLIC_YANDEX_TOKEN || config.public?.YANDEX_TOKEN || ''

  if (!apiKey) {
    return
  }

  const mod = await import('vue-yandex-maps').catch(() => null)
  if (!mod) return

  const createYmaps = (mod as any).createYmaps ?? (mod as any).createYmapsVue ?? (mod as any).createYmapsVue2
  const initYmaps = (mod as any).initYmaps
  const YmapPlugin = (mod as any).default ?? (mod as any).YmapPlugin ?? mod

  const settings = {
    apikey: apiKey,
    apiKey,
  }

  try {
    if (typeof createYmaps === 'function') {
      nuxtApp.vueApp.use(createYmaps(settings))
      return
    } else if (typeof initYmaps === 'function') {
      await initYmaps(settings)
    }

    if (YmapPlugin) {
      nuxtApp.vueApp.use(YmapPlugin, settings)
    }
  } catch (err) {
    return
  }
})
