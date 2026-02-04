<script setup lang="ts">
const route=useRoute()
const $q = useQuasar()
const search = ref(route.query.search)
async function upload(file: string) {
  const res = await useNuxtApp().$UPLOAD('/receipts/upload/', {file})
  if(res){
    $q.notify({message:JSON.stringify(res), color: 'green', position:'bottom-left'})
  }
}
</script>

<template lang="pug">
  q-file(@update:model-value="upload" label="Choose JSON" outlined counter)
  q-input(v-model="search")
    template(v-slot:after)
      q-btn(@click="navigateTo({query:{search, tab:'receipts'}})" icon="mdi-magnify" )
      q-btn(@click="navigateTo({query:{tab:'receipts'}})" icon="mdi-close" )
  receipt-search(v-if="route.query.search")
  receipt-monthly(v-else-if="!route.query.year && !route.query.month")
  receipt-year-month(v-else)
</template>

<style scoped>

</style>