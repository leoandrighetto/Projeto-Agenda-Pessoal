<template>

</template>

<script setup>
import { storeToRefs } from 'pinia';
import jwlStore from '../stores/jwtStore';

const store = jwlStore();

const { jwtToken } = storeToRefs(store);

console.log(jwtToken.value)

</script>