<script setup lang="ts">

import {getRowColByIndex, type ISeaBattle} from "~/components/seabattle/index";

const game = defineModel<ISeaBattle>()
const {onClick} = defineProps<{ onClick: Function }>()

const field = computed(() => {
  if (!game.value) return []
  return Array.from(Array(game.value.rows * game.value.cols).keys())
      .map(idx => {
        const cell = game.value?.field_my.find((x) => x.index === idx)
        return cell || getRowColByIndex(game.value, idx)
      })
})
const cellSize =40
const cs = ref(`${cellSize}px`)
const fs = ref(`${cellSize*(game.value?.rows || 10)}px`)

</script>

<template lang="pug">
  div.field.flex.wrap
    div.cell.cursor-pointer(v-for="cell in field"
      :class="cell.clicked ? 'clicked': cell.isShip ? 'ship':cell.ship ? 'deny':''"
      @click="onClick(cell)"
    ) {{cell.ship}}

</template>

<style scoped lang="sass">
.clicked
  background-color: red

.ship
  background-color: blue

.deny
  background-color: silver

.field
  width: v-bind(fs)

  .cell
    width: v-bind(cs)
    height: v-bind(cs)
    border: 1px solid silver
</style>