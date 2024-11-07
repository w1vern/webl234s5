export const useCatalogStore = defineStore('catalogStore', {
    state: () => ({
      catalog: []
    }),
    actions: {
      async fetch() {
        const { data } = await useMyFetch('/api/catalog/')
        this.catalog = data.value
      }
    }
  })