<script setup lang="ts">
const route = useRoute()
const item = ref()
async function load(){
  item.value = await useNuxtApp().$GET(`/receipts/${route.query.id}/view`)
}
onMounted(load)
</script>

<template lang="pug">
  div(v-if='item')
    div.text-h6 {{item.org}}
    div {{item.address}}
    div.text-right.text-bold {{$priceFormat(item.sum)}}
    table
      tbody
        tr
          th Наименование
          th Количество
          th Цена
          th Сумма
        tr(v-for="(item, index) in item.items" :key="index")
          td {{item.name}}
          td.text-center {{item.quantity}}
          td.text-right {{$priceFormat(item.price)}}
          td.text-right {{$priceFormat(item.price * item.quantity)}}
</template>

<style scoped>

</style>