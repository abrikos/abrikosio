<script setup lang="ts">
import {type ICell, type ISeaBattle} from "~/components/seabattle/index";
import SeaBattleField from "~/components/seabattle/Sea-Battle-Field.vue";
import DialogAddShips from "~/components/seabattle/Dialog-Add-Ships.vue";

const route = useRoute()
const game = ref<ISeaBattle>()

async function load() {
  game.value = await useNuxtApp().$GET(`/seabattle/${route.query.id}`)
}

onMounted(load)
const cell = ref<ICell>()
const dialogAddShips = ref(false)

function prepareShipCells(game: ISeaBattle, args: ICell): ICell[] {
  if (!args.ship) return []
  const ship = []
  if (args.horizontal) {
    for (let col = args.col; col < args.col + args.ship; col++) {
      if (col >= game.cols) continue
      const index = (args.row) * game.cols + col
      ship.push({...args, col, isShip: true, index})
    }
  } else {
    for (let row = args.row; row < args.row + args.ship; row++) {
      if (row >= game.rows) continue
      const index = row * game.cols + args.col
      ship.push({...args, row, isShip: true, index})
    }
  }
  return ship;
}

function adddShip(args: ICell) {
  if (!game.value) return
  const cells = prepareShipCells(game.value, args)
  game.value.field_my.push(...cells)
  dialogAddShips.value = false
}

function showAddSipDialog(args: ICell) {
  if (game.value?.is_active) return
  cell.value = args
  dialogAddShips.value = true
}

const errorsMy = ref([])
const errorsOp = ref([])

async function submit() {
  if (!game.value) return
  errorsMy.value = []
  errorsOp.value = []
  const res = await useNuxtApp().$POST(`/seabattle/${game.value.id}/start/`, game.value.field_my)
  if (res.statusText) {
    errorsMy.value = res.data.my
    errorsOp.value = res.data.op
  } else {
    game.value = res
  }
}

async function random() {
  errorsMy.value = []
  errorsOp.value = []
  const res = await useNuxtApp().$GET(`/seabattle/${route.query.id}/random/`)
  if (res.statusText) {
    errorsMy.value = res.data.my
    errorsOp.value = res.data.op
  } else {
    game.value = res
  }
}

function clearField(cell: ICell) {
  if (!game.value) return
  game.value.field_my = game.value.field_my.filter(c => c.ship !== cell.ship)
}

async function strike(cell: ICell) {
  if(cell.strike) return
  const res = await useNuxtApp().$PATCH(`/seabattle/${route.query.id}/strike/`, cell)
  if (res) {
    game.value = res
  }
}


</script>

<template lang="pug">
  div.row
    div.col
      sea-battle-field(v-model="game" :on-click="showAddSipDialog" game-field="field_my")
      q-dialog(v-model="dialogAddShips" )
        dialog-add-ships(v-model="cell" :on-add-ship="adddShip" :field="game.field_my" :on-clear-field="clearField")
      div(v-if="!game?.is_active")
        q-btn(@click="submit" color="primary" ) Start Game
        q-btn(@click="random") Random
        q-btn(@click="game.field_my=[]") Clear
        div.text-red {{errorsMy.join(', ')}}
    div.col(v-if="game?.is_active")
      sea-battle-field(v-model="game" :on-click="strike" game-field="field_op_masked")
      div.text-red {{errorsOp.join(', ')}}
</template>

<style scoped>

</style>