<script setup>

import InputMask from "primevue/inputmask";
import Button from 'primevue/button';
import Password from 'primevue/password'

const incorrect_data = ref(false)
const form = ref({ phone: '', password: '' , password1: ''})
const error = ref('Incorrect phone or password')

const router = useRouter()

async function register() {

}


</script>

<template>
    <div class="login_page">
        <Header></Header>
        <div class="content_with_footer">
            <div class="content">
                <div class="login_form">
                    <div class="description">
                        <p>Регистрация</p>
                    </div>
                    <form class="form" @submit.prevent="Register">
                        <InputMask class="field_input" id="basic" v-model="form.phone" mask="+7 (999) 999-99-99"
                            placeholder="+7 (999) 999-99-99" />
                        <Password class="field_input" id="password" name="password" toggleMask placeholder="Пароль"
                            promptLabel="Введите пароль" weakLabel="Слабый пароль" mediumLabel="Обычный пароль"
                            strongLabel="Сильный пароль" type="password" v-model="form.password"></Password>
                        <Password class="field_input" id="password1" name="password1" toggleMask placeholder="Повторите пароль"
                            promptLabel="Введите пароль" weakLabel="Слабый пароль" mediumLabel="Обычный пароль"
                            strongLabel="Сильный пароль" type="password" v-model="form.password1"></Password>
                        <Button class="field_input" id="go_button" label="Зарегистрироваться" @click="login"></Button>
                        <!-- <p v-if="incorrect_data" class="auth_error">
                            {{ error }}
                        </p> -->
                    </form>
                </div>
                <NuxtLink to="/auth/login" class="login">
                    <p>Войти </p>
                </NuxtLink>

            </div>
            <Footer class="footer"></Footer>
        </div>
    </div>
</template>

<style scoped>
.footer {
    width: 100%;
}

.content_with_footer {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.content {
    display: flex;
    width: max-content;
    height: max-content;
    flex-grow: 1;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    align-content: center;
}

.login_page * {
    caret-color: transparent;
    border: none;
}


.login_form {
    background-color: var(--p-surface-200);
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
    text-align: center;
    gap: 1rem;
    padding: 1.5rem;
    border-radius: 0.3rem;
}

.form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    align-content: center;
    text-align: center;
    gap: 2rem;
    padding: 1rem;
}

.description {
    font-size: 2rem;
    user-select: none;
}

.field_input {
    width: 100%;
    box-sizing: border-box;
    color: var(--p-surface-800);
    height: 1.8rem;
}


#go_button {
    width: 60%;
    color: var(--p-surface-50);
}

.form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    justify-content: center;
}

.remember_me_container {
    width: max-content;
    font-size: 18px;
}

.remember_me_container input[type="checkbox"]:checked::before {
    content: "\2714";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 13px;
}

.auth_error {
    color: red;
    font-size: 15px;
}


.login {
    user-select: none;
    font-size: 20px;
    padding: 10px;
    color: var(--p-surface-950);
    text-decoration: none;
    font-weight: 900;
}

.login:hover {
    color: var(--p-surface-500);
}
</style>
