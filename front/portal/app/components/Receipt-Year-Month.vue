<script setup lang="ts">
const route=useRoute()
console.log(route)

const list = ref([])

async function load() {
  list.value = await useNuxtApp().$GET('/receipts/year_month?'+new URLSearchParams(route.query as any).toString())
}

onMounted(load)

</script>

<template lang="pug">
  div
    router-link(to="/users/cabinet") Помесячно
  div.text-h3 {{ route.query.year }}-{{ route.query.month }}
  table
    tbody
      tr
        th Орг
        th Адрес
        th Сумма
        th Дата

      tr(v-for="(row, i) in list" :class="i % 2 ? 'bg-grey-4':''")
        td {{ row.org }}
        td {{ row.address }}
        td.text-right {{ $priceFormat(row.sum)}}
        td.text-right {{ row.date }}

</template>

<style scoped>

</style>