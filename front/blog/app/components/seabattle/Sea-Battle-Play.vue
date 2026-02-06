<script setup lang="ts">
import {type ICell, type ISeaBattle, prepareShipCells} from "~/components/seabattle/index";
import SeaBattleField from "~/components/seabattle/Sea-Battle-Field.vue";
import DialogAddShips from "~/components/seabattle/Dialog-Add-Ships.vue";

const route = useRoute()
const game = ref<ISeaBattle>()

async function load() {
  game.value = await useNuxtApp().$GET(`/seabattle/${route.query.id}/play`)
  adddShip({row: 0, col: 1, ship: 1})
  adddShip({row: 7, col: 7, ship: 2, horizontal: true})
  adddShip({row: 5, col: 0, ship: 3, horizontal: true})
  adddShip({row: 3, col: 3, ship: 4, horizontal: false})
  adddShip({row: 5, col: 5, ship: 5, horizontal: true})
  adddShip({row: 1, col: 5, ship: 5, horizontal: true})
}

onMounted(load)
const cell = ref<ICell>()
const dialogAddShips = ref(false)

function adddShip(args: ICell) {
  if (!game.value) return
  const cells = prepareShipCells(game.value, args)
  game.value.field_my.push(...cells)
  dialogAddShips.value = false
}

function showAddSipDialog(args: ICell) {
  if (args.ship) return
  cell.value = args
  dialogAddShips.value = true
}

const errors = ref([])

async function submit() {
  errors.value = []
  const res = await useNuxtApp().$POST('/seabattle/check_field/', game.value.field_my)
  if (res.statusText) {
    errors.value = res.data
  }
}


</script>

<template lang="pug">
  div(v-if="!game?.is_active")
    sea-battle-field(v-model="game" :on-click="showAddSipDialog")
    q-dialog(v-model="dialogAddShips" )
      dialog-add-ships(v-model="cell" :on-add-ship="adddShip" :field="game.field_my")
  q-btn(@click="submit") Check
  div {{errors}}
</template>

<style scoped>

</style>