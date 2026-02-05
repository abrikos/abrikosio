<script setup lang="ts">
const rows = 10
const cols = 10


interface ICell {
  row: number
  col: number
  index?: number
  ship?: number
  horizontal?: boolean
  isShip?: boolean
}

const defaultField = () => Array.from(Array(rows * cols).keys()).map(i => getRowCol(i))
const field = ref<ICell[]>(defaultField())

function getRowCol(index: number) {
  return {
    row: Math.floor(index / cols),
    col: index % rows,
    index
  }
}


</script>

<template lang="pug">
  div.text-h2 Sea battle
  div.field.flex.wrap
    div.cell.cursor-pointer(v-for="cell in field" :class="cell.clicked ? 'clicked': cell.isShip ? 'ship':cell.ship ? 'deny':''")

</template>

<style scoped lang="sass">
.clicked
  background-color: red
.ship
  background-color: blue

.deny
  background-color: silver

.field
  width: 400px

  .cell
    width: 40px
    height: 40px
    border: 1px solid silver
</style>