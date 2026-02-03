<script setup lang="ts">
async function upload(file){
  console.log(file)
  await useNuxtApp().$POST('/receipts/upload',file)
}
</script>

<template lang="pug">
  q-file(@update:model-value="upload" label="Choose JSON" outlined counter)
</template>

<style scoped>

</style>