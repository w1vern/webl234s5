<script setup>

const router = useRouter()
const authStore = useAuthStore()
const basketStore = useBasketStore()
const toast = useToast();

const isOpen = ref(true)
const popup = ref(null)

async function to_login() {
	router.push('/auth/login')
}

async function logout() {
	await authStore.logout()
}

async function close_basket() {
	basketStore.visible = false;
}

async function open_basket() {
	if (basketStore.basket.length == 0) {
		toast.add({ summary: "Ошибка", severity: "error", detail: "Корзина пуста", life: 3000 })
		return
	}
	basketStore.visible = true;
}

async function activate_promo() {
	if (basketStore.promos.includes(sale_value.value)) {
		basketStore.sale_activate = true
	}
	else {
		toast.add({ summary: "Ошибка", severity: "error", detail: "Промокод не найден", life: 3000 })
	}
	sale_value.value = ''
}

const sale_value = ref('')


</script>

<template>
	<div class="header_container">
		<div class="header">
			<div class="left">
				<div class="default">
					<NuxtLink to="/">
						<img src="~/assets/img/logo.svg" alt="logo" class="logo">
					</NuxtLink>
				</div>
				<div class="pages">
					<div class="about ">
						<NuxtLink to="/about" class="default_left">
							<p>
								О Нас
							</p>
						</NuxtLink>
					</div>
					<div class="contacts ">
						<NuxtLink to="/contacts" class="default_left">
							<p>
								Контакты
							</p>
						</NuxtLink>
					</div>
					<div class="catalog ">
						<NuxtLink to="/catalog" class="default_left">
							<p>
								Каталог
							</p>
						</NuxtLink>
					</div>
				</div>
			</div>
			<div class="right">
				<div class="basket_button_container" v-if="authStore.isAuth">
					<p class="basket_button" @click="open_basket" v-if="authStore.isAuth">
						<i class="pi pi-cart-arrow-down basket_icon">
							<p class="basket_count" v-if="basketStore.products_count > 0">
								{{ basketStore.products_count }}
							</p>
						</i>
					</p>
				</div>
				<div class="login default default_right" v-if="!authStore.isAuth">
					<Button class="login_button" label="Войти" @click="to_login"></Button>
				</div>
				<div class="login default default_right" v-else>
					<Button class="login_button" :label="authStore.phone" @click="logout"></Button>
				</div>
			</div>

		</div>
		<div class="basket_container" v-if="basketStore.visible">
			<div class="basket_element">
				<div class="basket">
					<table class="products">
						<div class="product" v-for="product in basketStore.basket">
							<div class="delete_product_container product_part">
								<p class="delete_product" @click="basketStore.set_count(product.id, 0)">
									<i class="pi pi-times"></i>
								</p>
							</div>
							<div class="image_container product_part">
								<img class="image" :src="product.path_to_image" alt="image">
							</div>
							<div class="info product_part">
								<p class="label">{{ product.label }}</p>
								<p class="description"> {{ product.description }}</p>
							</div>
							<div class="count_pick_container product_part">
								<CountPick class="count_pick" :max_value="product.can_be_ordered"
									v-model="product.count" :set_count_func="product.set_count"></CountPick>
							</div>
							<div class="price product_part">
								<p class="local_price_without_sale price_without_sale"
									v-if="!(product.sale * basketStore.sale_activate)">{{
										product.price*product.count }} ₽</p>
								<div class="local_price_with_sale price_with_sale" v-else>
									<p class="full_price">{{ product.price * product.count }} ₽</p>
									<p class="sale_price">{{ (product.price - product.sale_size) * product.count }} ₽
									</p>
								</div>
							</div>
						</div>
					</table>
					<div class="right_part">
						<div class="global_price">
							<p class="global_price_without_sale price_without_sale"
								v-if="!(basketStore.global_sale * basketStore.sale_activate)">Итого:
								{{ basketStore.global_price }} ₽</p>
							<div class="global_price_with_sale price_with_sale" v-else>
								<p class="text">Итого:</p>
								<div class="price_container">
									<p class="full_price">
										{{ basketStore.global_price }} ₽
									</p>
									<p class="sale_price">{{ basketStore.global_price - basketStore.global_sale }} ₽</p>
								</div>
							</div>
						</div>
						<div class="promo_field">
							<InputGroup class="input_group">
								<InputGroupAddon class="input_group_addon">
									<InputText v-model="sale_value" placeholder="Промо-код"></InputText>
								</InputGroupAddon>
								<InputGroupAddon class="input_group_addon">
									<Button label="Применить" severity="secondary" @click="activate_promo"></Button>
								</InputGroupAddon>
							</InputGroup>
						</div>
					</div>
					<div class="close_basket" @click="close_basket">
						<i class="pi pi-times"></i>
					</div>
				</div>

			</div>

		</div>
	</div>

</template>

<style scoped>
.header {
	display: flex;
	justify-content: space-between;
	width: 100%;
	position: fixed;
	background-color: var(--p-surface-200);
	color: var(--p-surface-950);
	z-index: 1;
	border-bottom: solid var(--p-surface-600) 0.01rem;
}

.default {
	padding: 1.5rem;
}

.left {
	display: flex;
}

.right {
	display: flex;
}

.pages {
	display: flex;
	gap: 2rem;
	align-items: center;
}

.logo {
	height: 2.5rem;
	transition: filter 0.3s ease;
}

.logo:hover {
	filter: brightness(1.5);
}

.login_button {
	font-size: 1.5rem;
	margin-right: 2.5rem;
}

.default_left {
	font-size: 1.5rem;
	color: var(--p-surface-950);
	text-decoration: none;
}

.default_left:hover {
	color: var(--p-surface-500);
	padding-top: 1rem;
}

.default_left:active {
	color: var(--p-primary-400);
}

.basket_button_container {
	display: flex;
	align-items: center;
	justify-content: center;
}

.basket_button {
	padding: 0.75rem;
	border-radius: 2rem;
	background-color: var(--p-surface-200);
}

.basket_icon {
	font-size: 1.5rem;
	position: relative;
}

.basket_count {
	position: absolute;
	top: -0.7rem;
	right: -0.7rem;
	font-size: 1rem;
	background-color: var(--p-primary-400);
	border-radius: 50%;
	height: 1.4rem;
	width: 1.4rem;
	line-height: 1.4rem;
	display: flex;
	align-items: center;
	justify-content: center;
}


.basket_button:hover {
	background-color: var(--p-surface-300);
	border-radius: 50%;
}

.basket_container {
	position: fixed;
	top: 0;
	left: 0;
	width: 100vw;
	height: 100vh;
	background-color: rgba(0.5, 0.5, 0.5, 0.5);
	display: flex;
	align-items: center;
	justify-content: center;
	z-index: 2;
}



.basket {
	position: relative;
	display: flex;
	flex-direction: row;
	padding: 3rem;
	gap: 3rem;
	background-color: var(--p-surface-200);
	border-radius: 1rem;
	width: 80vw;
	height: max-content;
	min-height: 60vh;
}

.close_basket {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	position: absolute;
	top: 1rem;
	right: 1rem;
	font-size: 2rem;
	padding: 0.5rem;
	cursor: pointer;
}

.close_basket:hover {
	background-color: var(--p-surface-300);
	border-radius: 50%;
}

.products {
	width: 80%;
	height: 100%;
	display: flex;
	flex-direction: column;
	gap: 1rem;
}

.product {
	display: flex;
	flex-direction: row;
	gap: 2rem;
	background-color: var(--p-surface-100);
	padding: 1rem;
	border-radius: 1rem;
	height: 10rem;
}

.product_part {
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.image_container {
	width: 15%;
	display: flex;
	justify-content: center;
}

.image {
	width: auto;
	height: 100%;
	border-radius: 1rem;
}

.info {
	width: 40%;
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
}

.label {
	font-size: 1.5rem;
}

.description {
	font-size: 1.1rem;

}

.count_pick_container {
	width: 20%;
}

.count_pick {
	margin-left: 5rem;
	height: 3rem;
}

.price {
	width: 25%;
	height: auto;
}

.full_price {
	color: var(--p-surface-500);
	text-decoration: line-through;
	font-size: 1rem;
}

.sale_price {
	font-size: 2rem;
	color: var(--p-surface-900);
}

.global_price_with_sale {
	display: flex;
	flex-direction: row;
	align-content: center;
	justify-content: center;
	gap: 2rem;
	margin-top: 2rem;
}

.text {
	font-size: 3rem;
}

.price_container {
	display: flex;
	flex-direction: column;
}

.right_part {
	display: flex;
	flex-direction: column;
	gap: 2rem;
}

.price_without_sale {
	font-size: 2rem;
	color: var(--p-surface-900);
	border-radius: 1.5rem;
}

.delete_product {
	padding: 0.5rem;
}

.delete_product:hover {
	background-color: var(--p-surface-300);
	border-radius: 50%;
}
</style>
