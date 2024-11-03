<script setup>

const router = useRouter()

const authStore = useAuthStore()

async function to_login() {
    router.push('/auth/login')
}

async function logout()
{
    await authStore.logout()
}

</script>

<template>
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
            <div class="login default default_right" v-if="!authStore.isAuth">
                <Button class="login_button" label="Войти" @click="to_login"></Button>
            </div>
            <div class="login default default_right" v-else>
                <Button class="login_button" :label="authStore.phone" @click="logout"></Button>
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
    padding-top: rem;
}

.default_left:active
{
    color: var(--p-primary-400);
}
</style>