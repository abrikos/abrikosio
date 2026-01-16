<script setup lang="ts">
import axios from 'axios';

async function token(){
  return await axios.post('/token')
}
</script>

<template lang="pug">
  q-page
    q-btn(@click="token") test

</template>

<style scoped>

</style>
