<script setup lang="ts">
const list = ref([])

async function load() {
  list.value = await useNuxtApp().$GET('/receipts/monthly')
}

onMounted(load)

</script>

<template lang="pug">
  table
    tbody
      tr
        th Год
        th Месяц
        th Сумма
        th Кол-во

      tr(v-for="row in list" :class="row.year % 2 ? 'bg-grey-4':''")
        td.text-center {{ row.year }}
        td.text-center
          router-link(:to="{query:{year:row.year, month:row.month}}") {{ $getMonthName(row.month) }}
        td.text-right {{ $priceFormat(row.sum)}}
        td.text-right {{ row.count }}

</template>

<style scoped>

</style>