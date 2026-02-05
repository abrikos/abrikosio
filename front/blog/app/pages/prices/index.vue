<script setup lang="ts">
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const list = ref([])
const route = useRoute()

async function load() {
  if (search.value) {
    const res = await useNuxtApp().$GET('/receipts/goods?search=' + search.value)
    if (res) list.value = res
  }
}

onMounted(load)
const initialPagination = {
  sortBy: 'desc',
  descending: false,
  page: 1,
  rowsPerPage: 10
  // rowsNumber: xx if getting data from a server
}

const search = ref(route.query.search)

function doSearch() {
  navigateTo({query: {search: search.value}})
  load()
}

const goods = ref([])
const goodsTitle = ref()
const goodsDialog = ref(false)
const chartData = computed(()=>({
  labels: goods.value.map(x=> {
    const split = x.date.split('T')
    return split[0]
  }),
  datasets: [{label: goodsTitle.value, backgroundColor:'red', data: goods.value.map(x => x.price)}],
}))

async function showChart(e: PointerEvent, row: { name: string }) {
  const res = await useNuxtApp().$GET('/receipts/goods_list?search=' + row.name)
  if(!res) return
  goodsTitle.value = row.name
  console.log(res.reverse())
  goods.value = res.reverse()
  goodsDialog.value = !!goods.value

}

</script>

<template lang="pug">
  q-dialog(v-model="goodsDialog")
    q-card(style="width: 100%")
      q-card-section
        Bar#chart(:data="chartData" aria-label="zzzzzzz")

  q-input(v-model="search" placeholder="Поиск..." @keyup.enter.native="doSearch")
    template(v-slot:after)
      q-btn(@click="doSearch" icon="mdi-magnify" )
      q-btn(@click="navigateTo({query:{tab:'receipts'}})" icon="mdi-close" )
  q-table(:rows="list" :pagination="initialPagination" @row-click="showChart")
</template>

<style scoped>

</style>