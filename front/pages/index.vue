
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import InputMask from "primevue/inputmask";
import Button from 'primevue/button';

const incorrect_data = ref(false)
const form = ref({ phone: '', password: '' })
const error = ref('Incorrect login or password')

const router = useRouter()

async function to_register() {
    
}

/* async function SignIn() {
    const data = await apiUsersLogin(form)
    if (data == 200) {
        const loginStore = UseLoginStore()
        await loginStore.fetch()
        router.push('/lobby')
    } else {
        incorrect_data.value = true
    }
} */


</script>

<template>
    <div class="login_page">
        <div class="login_form">
            <div class="description">
                <p>Auth</p>
            </div>
            <div class="form">
                <form class="form" @submit.prevent="SignIn">
                    <p>
                        <InputMask id="basic" v-model="form.phone" mask="+7(999)-999-99-99" placeholder="+7(999)-999-99-99"/>
                    </p>
                    <p>
                        <input class="field_input" id="password" name="password" placeholder="Password" required=""
                            type="password" v-model="form.password">
                    </p>
                    <p>
                        <Button label="Войти" @click="to_register"></Button>
                    </p>
                    <p v-if="incorrect_data" class="auth_error">
                        {{ error }}
                    </p>
                </form>
            </div>
        </div>
        <a href="/register" class="register">Sign Up</a>
    </div>
</template>

<style scoped>
.login_page {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-content: center;
    align-items: center;
    height: 100%;
}

.login_page * {
    caret-color: transparent;
    border: none;
}

.login_page * ::selection {
    background-color: #550066;
}

.login_form {
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    font-size: 20px;
    background-color: #111010;
    gap: 16px;
}

.description {
    font-size: 28px;
    user-select: none;
}

.field_input {
    box-sizing: border-box;
    width: 180px;
    height: 30px;
    border-radius: 3px;
    background-color: #222020;
    color: #ffffff;
    padding: 2px 8px 2px 8px;
}

.field_input:focus {
    caret-color: #9900aa;
    outline: 2px solid #550066;
}

.form {
    background-color: #111010;
    display: flex;
    flex-direction: column;
    gap: 16px;
    justify-content: center;
}

.remember_me_container {
    width: max-content;
    font-size: 18px;
}

.remember_me_container input[type="checkbox"] {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 14px;
    height: 14px;
    border: 2px solid #550066;
    border-radius: 3px;
    outline: none;
    cursor: pointer;
    position: relative;
}

.remember_me_container input[type="checkbox"]:checked::before {
    content: "\2714";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 13px;
    color: #9900aa;
}

.auth_error {
    color: red;
    font-size: 15px;
}


.register {
    user-select: none;
    font-size: 20px;
    padding: 10px;
    color: #880099;
    text-decoration: none;
    font-weight: 900;
}

.register:hover {
    color: #aa00bb;
}
</style>
