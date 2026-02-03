<script setup lang="ts">
const $q = useQuasar()
async function upload(file: string) {
  const res = await useNuxtApp().$UPLOAD('/receipts/upload/', {file})
  if(res){
    $q.notify({message:JSON.stringify(res), color: 'green', position:'bottom-left'})
  }
}
</script>

<template lang="pug">
  q-file(@update:model-value="upload" label="Choose JSON" outlined counter)
</template>

<style scoped>

</style>