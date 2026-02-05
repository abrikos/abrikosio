<script setup lang="ts">
const rows = 10
const cols = 10


interface ICell {
  row: number
  col: number
  ship?: number
  horizontal?: boolean
  isShip?: boolean
}

const data = ref<[ICell?]>([])

function place(args: ICell) {
  if (!validateCell(args) || !args.ship || !field.value) return

  const cell = getCell(args)
  if (!cell) return

  const shipCells = prepareShipCells(args)
  if (!shipCells) return
  for (const shipCell of shipCells) {
    const cell = getCell(shipCell)
    cell && (cell.isShip = true)
  }
  for (const ship of shipCells) {
    for (let row = ship.row - 1; row <= ship.row + 1; row++) {
      for (let col = ship.col - 1; col <= ship.col + 1; col++) {
        const cell = getCell({row, col})
        if (!cell) continue
        cell.ship = args.ship
      }
    }
  }
}

function prepareShipCells(args: ICell): ICell[] {
  if (!args.ship) return []

  const ship = []

  if (args.horizontal) {
    for (let col = args.col; col < args.col + args.ship; col++) {
      ship.push({...args, col, isShip: true})
    }
  } else {
    for (let row = args.row; row < args.row + args.ship; row++) {
      ship.push({...args, row, isShip: true})
    }
  }
  return ship;
}

function validateCell(args: ICell): boolean {
  if (!args.ship) return false
  const shipCells = prepareShipCells(args)
  for (const ship of shipCells) {
    const cell = getCell(ship)
    if (!cell) return false
    if (cell.ship) return false
  }
  return !!shipCells.length
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
  }
}

function clearShip(args: ICell) {
  if (!args.ship) return
  field.value = field.value.map(c => {
    return c.ship === args.ship ? {...c, ship: 0, deny: false, isShip: false} : c
  })
}

const defaultField = () => Array.from(Array(rows * cols).keys()).map(i => getRowCol(i))
const field = ref<ICell[]>(defaultField())
const field2 = ref<ICell[]>([])

function clearField() {
  field.value = defaultField()
}

onMounted(() => {
  place({row: 0, col: 1, ship: 1})
  place({row: 7, col: 7, ship: 2, horizontal: true})
  place({row: 5, col: 1, ship: 3, horizontal: true})
  place({row: 3, col: 3, ship: 4, horizontal: true})
  place({row: 5, col: 5, ship: 5, horizontal: true})
})

function random() {
  clearField()
  for (let ship = 1; ship < 6; ship++) {
    const horizontal = Math.random() > 0.5
    const free = field.value.filter(c => !c.ship && validateCell({...c, horizontal, ship}))
    const randomIndex = Math.floor(Math.random() * free.length);
    const cell = free[randomIndex]
    if(cell && cell.row && cell.col)
      place({...cell, ship, horizontal})
  }

}

const errors = ref([])

async function submit() {
  errors.value = []
  const res = await useNuxtApp().$POST('/seabattle/check_field/', field.value.filter(c => c.isShip))
  if (res.statusText) {
    errors.value = res.data
  }else{
    field2.value = res
  }
}

</script>

<template lang="pug">
  div.text-h2 Sea battle
  div.field.flex.wrap
    div.cell.cursor-pointer(v-for="cell in field" :class="cell.clicked ? 'clicked': cell.isShip ? 'ship':cell.ship ? 'deny':''") {{cell.ship}}
      q-popup-proxy(@before-show="cell.clicked=true" @before-hide="cell.clicked=false" )
        span {{cell}}
        table
          tbody
            tr
              th
              th Horizontal
              th Vertical
            tr(v-for="ship in 5" v-if="!cell.ship")
              td {{ship}}
              td(v-for="horizontal in [true,false]" )
                q-btn(@click="place({...cell, horizontal, ship})" v-if="validateCell({...cell, horizontal, ship})" :icon="horizontal ? 'mdi-arrow-right':'mdi-arrow-down'" )
        q-btn(@click="clearShip(cell)") Clear
  q-btn(@click="clearField") Clear Field
  q-btn(@click="random") Random
  q-btn(@click="submit") Check
  div.text-red(v-for="e in errors" ) {{e}}

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