<script setup lang="ts">
const route=useRoute()
const list = ref([])
const large = ref()

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
      th Наименование
      th Кол-во
      th Цена
      th Сумма
    tr(v-for="item in list" )
      td.name
        q-btn(size="sm" icon="mdi-resize" @click="large ? large=null : large=item.id")
        b {{ item.name }}
        div(v-if="large===item.id")
          div.text-caption {{ item.place.split(',').join(' ') }}
          div.text-caption  {{ item.org.split(',').join(' ') }}
          div.text-caption  {{ item.address.split(',').join(' ') }}
        div.text-caption {{ item.date }}
      td.text-center {{ item.quantity }}
      td.text-right {{ $priceFormat(item.price) }}
        div.text-indigo(v-if="!Number.isInteger(item.quantity)")
          small {{ $priceFormat(item.price/item.quantity) }}
      td.text-right.text-bold {{ $priceFormat(item.price * item.quantity) }}


</template>

<style scoped lang="sass">
table
  tr
    font-size: .8em
  td.name
    //display: none
    width: 30%
</style>