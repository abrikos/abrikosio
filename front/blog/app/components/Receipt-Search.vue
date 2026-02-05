<script setup lang="ts">
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const route=useRoute()
const list = ref([])
const large = ref()

async function load() {
  list.value = await useNuxtApp().$GET('/receipts/search?'+new URLSearchParams(route.query as any).toString())
}

onMounted(load)
watch(() => route.query.search, load)

const goods = ref([])
const goodsTitle = ref()
const goodsDialog = ref(false)
const chartData = computed(()=>({
  labels: goods.value.map(x=> {
    const split = x.date.split(' ')
    return split[0]
  }),
  datasets: [{label: goodsTitle.value, backgroundColor:'red', data: goods.value.map(x => x.price)}],
}))
async function goodPrices(name:string){
  const list = await useNuxtApp().$GET('/receipts/search?search='+name)
  goodsTitle.value = name
  goods.value = list.reverse()
  goodsDialog.value = !!goods.value

}
</script>

<template lang="pug">
q-dialog(v-model="goodsDialog")
  q-card(style="width: 100%")
    q-card-section
      Bar#chart(:data="chartData" aria-label="zzzzzzz")
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
        q-btn(size="sm" @click="goodPrices(item.name)") {{ item.name }}
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