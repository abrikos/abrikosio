<script setup lang="ts">
const route=useRoute()
const list = ref([])

async function load() {
  list.value = await useNuxtApp().$GET('/receipts/search?'+new URLSearchParams(route.query as any).toString())
}

onMounted(load)
watch(() => route.query.search, load)
</script>

<template lang="pug">
table
  tbody
    tr
    tr(v-for="item in list" )
      td {{ item.date }}
      td {{ item.name }}
      td.text-center {{ item.quantity }}
      td.text-right {{ $priceFormat(item.price) }}
      td {{ item.place || item.address || item.org }}
</template>

<style scoped>

</style>