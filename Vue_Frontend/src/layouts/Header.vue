<script setup>

</script>

<template>
    <v-app-bar color="blue" density="compact" :elevation="0">
        <template #prepend>
            <v-app-bar-nav-icon @click="$emit('drawer')" />
        </template>

        <v-app-bar-title>
            Agenda Pessoal
        </v-app-bar-title>

        <template #append>
            <v-btn icon="mdi-heart" />
            <v-btn icon="mdi-magnify" />
            <v-btn icon="mdi-dots-vertical" />
        </template>
    </v-app-bar>
</template>

<style scoped>
/* Evite layout manual aqui */
</style>