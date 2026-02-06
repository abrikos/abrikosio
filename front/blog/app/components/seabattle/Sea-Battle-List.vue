<script setup lang="ts">
import type {ISeaBattle} from "~/components/seabattle/index";
import UserAvatar from "~/components/user/UserAvatar.vue";

const route = useRoute()
const games = ref<ISeaBattle[]>([])

async function load() {
  games.value = await useNuxtApp().$GET(`/seabattle`)
}

onMounted(load)

async function create() {
  const query = await useNuxtApp().$GET(`/seabattle/start`)
  if (!query || query.statusText) return
  navigateTo({query})
}

const cols = [
  {field: 'dimension', label: 'Dimension', format: (v: any, r: ISeaBattle) => `${r.rows}x${r.cols}`},
  {field: 'user', label: 'User', name: 'user'},
  {field: 'date', label: 'Date', name: 'date'},
]
function goToGame(id:number) {
  console.log(id)
}
</script>

<template lang="pug">
  q-btn(@click="create") Create
  q-table(:rows="games" :columns="cols" @row-click="(e,row)=>navigateTo({query:{id:row.id}})")
    template(v-slot:body-cell-user="{row}")
      UserAvatar(:user="row.user")
</template>

<style scoped>

</style>