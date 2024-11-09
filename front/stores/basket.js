export const useBasketStore = defineStore('basketStore', {
	state: () => ({
		basketFromBack: [],
		basket: [],
		global_price: 0,
		global_sale: 0,
		products_count: 0,
		visible: false,
		promos: ['sale'],
		sale_activate: false
	}),
	actions: {
		async fetch_state() {
			const catalogStore = useCatalogStore()
			this.products_count = 0
			this.global_price = 0
			this.global_sale = 0
			const { data: api_catalog_basket } = await useMyFetch('/api/catalog/basket');
			this.basketFromBack = api_catalog_basket.value;
			await catalogStore.fetch()
			this.basket = this.basketFromBack.products;
			this.basket.forEach(product => {
				let one_product_info = catalogStore.catalog.find((a) => a.id == product.id)
				product.label = one_product_info.label
				product.description = one_product_info.description
				product.path_to_image = one_product_info.path_to_image
				product.price = one_product_info.price
				product.sale = one_product_info.sale
				product.sale_size = product.price * product.sale
				product.set_count = (count) => this.set_count(product.id, count)
				this.global_price += product.price * product.count
				this.global_sale += product.sale_size * product.count
				this.products_count += product.count
			})
			if (this.products_count == 0) {
				this.visible = false
			}
		},

		async send_state() {
			const { data } = await useMyFetch('/api/catalog/new_basket_state', {
				method: "post",
				body: this.basketFromBack
			});
		},
		async add_product(product_id) {
			let index = this.basketFromBack.products.findIndex(product_in => product_in.id == product_id)
			if (index != -1) {
				this.basketFromBack.products[index].count += 1
			}
			else {
				this.basketFromBack.products.push({ id: product_id, count: 1 })
			}
			await this.send_state()
			await this.fetch_state()
		},

		async set_count(product_id, count) {
			let index = this.basketFromBack.products.findIndex(product_in => product_in.id == product_id)
			if (index == -1)
				return
			else {
				this.basketFromBack.products[index].count = count
				await this.send_state()
				await this.fetch_state()
			}
	}
}
})
