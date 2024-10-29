<script setup>

</script>

<template>
    <div class="header">
        <div class="left">
            <div class="logo default">
                <NuxtLink to="/">
                    <img src="~/assets/img/logo.svg" alt="logo">
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
                <NuxtLink to="/auth/login">
                    <p>
                        Вход
                    </p>
                </NuxtLink>
            </div>
            <div class="register default default_right">
                <NuxtLink to="/auth/register">
                    <p>
                        Регистрация
                    </p>
                </NuxtLink>
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
    background-color: var(--p-surface-950);
    color: var(--p-surface-50)
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
</style>