<script setup lang="ts">

import {type ICell, type ISeaBattle} from "~/components/seabattle/index";

const game = defineModel<ISeaBattle>()
const {onClick, gameField} = defineProps<{ onClick: Function, gameField:string }>()

///console.log('zzzzzzzz', typeof game.value === ISeaBattle)

const field = computed(() => {
  if (!game.value || !game.value[gameField]) return []
  return Array.from(Array(game.value.rows * game.value.cols).keys())
      .map(idx => {
        const cell = game.value[gameField].find((x:ICell) => x.index === idx)
        return cell || getRowColByIndex(game.value, idx)
      })
})
const cellSize =40
const cs = ref(`${cellSize}px`)
const fs = ref(`${cellSize*(game.value?.rows || 10)}px`)

function getRowColByIndex(game: ISeaBattle | undefined, index: number) {
  if (!game) return {}
  return {
    row: Math.floor(index / game.cols),
    col: index % game.rows,
    index
  }
}

const debug = true
function cellClass(cell:ICell) {
  if(cell.kill) return 'kill'
  if(cell.hit) return 'hit'
  if(cell.strike) return 'strike'
  if(cell.ship && cell.isShip) return 'ship'
  if(cell.ship && debug) return 'deny'
}

</script>

<template lang="pug">
  div.field.flex.wrap
    div.cell.cursor-pointer(v-for="cell in field" :class="cellClass(cell)" @click="onClick(cell)")
      div.flex.justify-center.items-center.full-height.text-white(vif="cell.isShip") {{debug ? cell.ship: ''}}
</template>

<style scoped lang="sass">
.clicked
  background-color: red

.ship
  background-color: blue

.deny
  background-color: silver

.kill
  background-color: red

.hit
  background-color: green

.strike
  background-color: red

.field
  width: v-bind(fs)

  .cell
    width: v-bind(cs)
    height: v-bind(cs)
    border: 1px solid silver

</style>