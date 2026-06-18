<script setup>
import '../../style.css';

import register from '../../services/user/auth';

import { ref } from 'vue';

const username = ref(null);
const full_name = ref(null)
const email = ref(null);
const password = ref(null);
const confirm_password = ref(null);



async function register_user() {

    const user_data = {
        "username": username.value,
        "fullname": full_name.value,
        "email": email.value,
        "password": password.value,
    }

    if (!username || !full_name.value || !email.value || !password.value || !confirm_password.value) {
        alert("Dados incompletos");
        return;

    } else if (password.value != confirm_password.value) {
        alert("As senhas não coincidem.")
        return;
    }

    try {

        const response = await register(user_data)

        alert(response.data);

        return;
    } catch (error) {
        return error;
    }

}


</script>

<template>
    <v-container>
        <div class="d-flex justify-center mt-16">
            <v-card class="d-flex flex-column align-center text-center geral-card bg-secondary" rounded="30">
                <div class="geral-card-title">
                    Inicie sua Agenda Pessoal
                </div>
                <div class="geral-card-content">
                    <v-text-field v-model="username" bg-color="white" class="geral-input" required
                        placeholder="Username" clearable rounded="10" variant="solo" type="text" />

                    <v-text-field v-model="full_name" bg-color="white" class="geral-input" required
                        placeholder="Nome completo" clearable rounded="10" variant="solo" type="text" />

                    <v-text-field v-model="email" bg-color="white" class="geral-input" required
                        placeholder="Seu melhor E-mail" clearable rounded="10" variant="solo" type="email" />

                    <v-text-field v-model="password" bg-color="white" class="geral-input" required placeholder="Senha"
                        clearable rounded="10" variant="solo" type="password" />

                    <v-text-field v-model="confirm_password" bg-color="white" class="geral-input" required
                        placeholder="Confirmar Senha" clearable rounded="10" variant="solo" type="password" />
                </div>
                <div>
                    <v-btn class="text-title-small" variant="text">Já possuo uma conta</v-btn>
                </div>
                <div>
                    <v-btn class="register-button bg-primary" @click="register_user" type="submit">Registrar</v-btn>
                </div>
            </v-card>
        </div>
    </v-container>
</template>

<style></style>