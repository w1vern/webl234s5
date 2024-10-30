<script setup>

const router = useRouter()

async function to_login() {
    router.push('/auth/login')
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
                <div class="about default default_left">
                    <NuxtLink to="/about">
                        <p>
                            О Нас
                        </p>
                    </NuxtLink>
                </div>
                <div class="contacts default default_left">
                    <NuxtLink to="/contacts">
                        <p>
                            Контакты
                        </p>
                    </NuxtLink>
                </div>
                <div class="catalog default default_left">
                    <NuxtLink to="/catalog">
                        <p>
                            Каталог
                        </p>
                    </NuxtLink>
                </div>
            </div>
        </div>
        <div class="right">
            <div class="login default default_right">
                <Button class="login_button" label="Войти" @click="to_login"></Button>
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
    background-color: var(--p-surface-700);
    color: var(--p-surface-50);
    z-index: 9999;
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
    gap: 1rem
}

.logo {
    height: 2.5rem;
}
</style>