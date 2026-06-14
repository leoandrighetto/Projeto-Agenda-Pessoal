<script setup>
import '../../style.css';



</script>

<template>
    <v-container>
        <div class="d-flex justify-center mt-16">
            <v-card class="d-flex flex-column align-center text-center geral-card bg-secondary" rounded="30">
                <div class="geral-card-title">
                    Inicie sua Agenda Pessoal
                </div>
                <div class="geral-card-content">
                    <v-text-field bg-color="white" class="geral-input" placeholder="Seu melhor E-mail" clearable
                        rounded="10" variant="solo" type="email" />

                    <v-text-field bg-color="white" class="geral-input" placeholder="Senha" clearable rounded="10"
                        variant="solo" type="password" />

                    <v-text-field bg-color="white" class="geral-input" placeholder="Confirmar Senha" clearable
                        rounded="10" variant="solo" type="password" />
                </div>
                <div>
                    <v-btn class="text-title-small" variant="text">Já possuo uma conta</v-btn>
                </div>
                <div>
                    <v-btn class="register-button bg-primary" type="submit">Registrar</v-btn>
                </div>
            </v-card>
        </div>
    </v-container>
</template>

<style></style>