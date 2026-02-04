<script setup lang="ts">
const route=useRoute()
const list = ref([])

async function load() {
  list.value = await useNuxtApp().$GET('/receipts/year_month?'+new URLSearchParams(route.query as any).toString())
}

onMounted(load)
const showDetail = computed(()=>!!route.query.id)
</script>

<template lang="pug">
  div
    router-link(:to="{query:{tab:'receipts'}}") Помесячно
  div.text-h3 {{ route.query.year }}-{{ route.query.month }}
  table
    tbody
      tr
        th Орг
        th Адрес
        th Сумма
        th Дата

      tr(v-for="(row, i) in list" :class="i % 2 ? 'bg-grey-4':''")
        td.cursor-pointer(@click="navigateTo({query:{...route.query, id:row.id}})") {{ row.org }}
        td {{ row.address }}
        td.text-right {{ $priceFormat(row.sum)}}
        td.text-right {{ row.date }}

  q-dialog(v-model="showDetail" persistent scrollable fullscreen)
    q-card
      q-toolbar
        q-space
        q-btn(icon="mdi-close" @click="navigateTo({query:{...route.query, id:null}})" flat)
      q-card-section
        receipt-detail
</template>

<style scoped>

</style>