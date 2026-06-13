<script setup>
import Header from './layouts/Header.vue';
import Drawer from './layouts/Drawer.vue';
import { ref } from 'vue';

const drawer = ref(false);

const toggle_drawer = () => {
  drawer.value = !drawer.value;
}


</script>

<template>
  <v-app>
    <Header @drawer="toggle_drawer"/>
    <Drawer v-model="drawer"/>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>
