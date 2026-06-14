<script setup>
import { ref, watch } from 'vue';
import { storeToRefs } from 'pinia';
import jwlStore from './stores/jwtStore.js';

import Header from './layouts/Header.vue';
import Drawer from './layouts/Drawer.vue';

const store = jwlStore();
const drawer = ref(false);

const has_token = ref(store.hasToken)

const toggle_drawer = () => {
  drawer.value = !drawer.value;
}

</script>

<template>
  <v-app>
    <div v-if="has_token">
      <Header @drawer="toggle_drawer" />
      <Drawer v-model="drawer" />
    </div>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>
