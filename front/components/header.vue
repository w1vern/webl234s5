<script setup>

const router = useRouter()
const authStore = useAuthStore()
const basketStore = useBasketStore()

const isOpen = ref(true)
const popup = ref(null)

async function to_login() {
	router.push('/auth/login')
}

async function logout()
{
	await authStore.logout()
}

async function close_basket() {
	basketStore.visible = false;
}

async function open_basket() {
	basketStore.visible = true;
}


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
				<div class="basket_button_container">
					<p class="basket_button" @click="open_basket">
						<OverlayBadge size="small" :value="basketStore.products_count" v-if="basketStore.products_count > 0" severity="danger">
					<i class="pi pi-cart-arrow-down basket_icon"></i>
				</OverlayBadge>
				<i class="pi pi-cart-arrow-down basket_icon" v-else></i>

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
	<Dialog class="basket_container" v-model:visible="basketStore.visible">
		<div class="basket_element">
			<div class="basket">
				<dic class="products">
					<div class="product" v-for="product in basketStore.products">
						<img :src="product.image" alt="image" class="image">
						<div class="info">
							<p class="label">{{ product.label }}</p>
							<p class="description"> {{ product.description }}</p>
						</div>
						<div class="price">
							<p class="local_price_without_sale price_without_sale" v-if="!product.sale">{{ product.price }} ₽</p>
							<div class="local_price_with_sale price_with_sale" v-else>
								<p>{{ product.price }} ₽</p>
								<p>{{ product.price - product.sale_size }} ₽</p>
							</div>
						</div>
					</div>
				</dic>
				<div class="global_price">
					<p class="global_price_without_sale price_without_sale" v-if="!basketStore.global_sale">Итого: {{ basketStore.global_price }} ₽</p>
					<div class="global_price_with_sale price_with_sale" v-else>
						<p>Итого: {{ basketStore.global_price }} ₽</p>
						<p>{{ basketStore.global_price - basketStore.global_sale_size }} ₽</p>
					</div>
				</div>
			</div>
		</div>
	</Dialog>
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
	z-index: 9999;
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
	filter: brightness(1.5); /* Увеличение яркости */
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

.default_left:active
{
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

.basket_icon
{
	font-size: 1.5rem;
}


.basket_button:hover{
	background-color: var(--p-surface-500);
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
	z-index: 1000;
}

.basket_element {


}

.basket {
	display: flex;
	flex-direction: row;
	padding: 5rem;
	gap: 3rem;
}

.products {
	display: flex;
	flex-direction: column;
	gap: 2rem;
}

.product {
	display: flex;
	flex-direction: row;
	gap: 2rem;
}

.info {
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
}


</style>
