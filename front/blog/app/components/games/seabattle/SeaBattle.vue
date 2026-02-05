<script setup lang="ts">
const rows = 10
const cols = 10


interface ICell {
  row: number
  col: number
  ship?: number
  horizontal?: boolean
  deny?: boolean
  isShip?: boolean
}

const data = ref<[ICell?]>([])

function cellClass(cell: ICell) {
  return cell.ship ? 'selected' : cell.deny ? 'deny' : ''
}

function place(args: ICell) {
  if (!validateCell(args) || !args.ship || !field.value) return console.log(validateCell(args), args.ship, field.value)
  const cell = getCell(args)
  if (!cell || cell.ship || cell.deny) return
  for (let i = 0; i < args.ship; i++) {
    const index = getIndex(args) + (args.horizontal ? i : i * 10)
    if (!field.value[index]) continue
    field.value[index].isShip = true
    field.value[index].ship = args.ship
  }
  const shipCells = field.value.filter(c => c.ship === args.ship)
  for (const ship of shipCells) {
    for (let row = ship.row - 1; row <= ship.row + 1; row++) {
      for (let col = ship.col - 1; col <= ship.col + 1; col++) {
        const cell = getCell({row,col})
        if (!cell) continue
        cell.deny = true
        cell.ship = args.ship
      }
    }
  }
}

function validateCell(args: ICell) {
  if (!args.ship) return
  const cell = getCell(args)
  if (!cell || cell.ship || cell.deny) return
  if (field.value.find(c => c.ship === args.ship)) return
  if (args.horizontal) {
    return cols - args.col - args.ship >= 0
  } else {
    return rows - args.row - args.ship >= 0
  }
}

function getIndex(cell: ICell) {
  return (cell.row) * cols + cell.col
}

function getCell(cell: ICell) {
  return field.value.find(c => c.col === cell.col && c.row === cell.row)
}

function getRowCol(index: number) {
  return {
    row: Math.floor(index / cols),
    col: index % rows,
    index
  }
}

function clearShip(args: ICell) {
  if (!args.ship) return
  field.value = field.value.map(c => {
    return c.ship === args.ship ? {...c, ship: 0, deny: false, isShip:false} : c
  })
}

const defaultField = () => Array.from(Array(rows * cols).keys()).map(i => getRowCol(i))
const field = ref<ICell[]>(defaultField())

function clearField() {
  field.value = defaultField()
}

onMounted(()=>place({row:7, col:9, ship:1}))

</script>

<template lang="pug">
  div.field.flex.wrap
    div.cell.cursor-pointer(v-for="cell in field" :class="cell.isShip ? 'ship':cell.deny ? 'deny':''") {{getIndex(cell)}}
      q-popup-proxy
        table
          tbody
            tr
              th
              th Horizontal
              th Vertical
            tr(v-for="ship in 5" )
              td {{ship}}
              td(v-for="horizontal in [true,false]" )
                q-btn(@click="place({...cell, horizontal, ship})" v-if="validateCell({...cell, horizontal, ship})" :icon="horizontal ? 'mdi-arrow-right':'mdi-arrow-down'" )
        q-btn(@click="clearShip(cell)") Clear
  q-btn(@click="clearField()") Clear Field
  div {{field.filter(c=>c.ship)}}

</template>

<style scoped lang="sass">
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