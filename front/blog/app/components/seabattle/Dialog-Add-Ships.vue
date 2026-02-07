<script setup lang="ts">
import type {ICell, ISeaBattle} from "~/components/seabattle/index";

const cell = defineModel<ICell>()
const {onAddShip, onClearField} = defineProps<{onAddShip:Function, onClearField:Function}>()


</script>

<template lang="pug">
  q-card
    q-card-section
      table
        tbody
          tr
            th
            th Horizontal
            th Vertical
          tr(v-for="ship in 5" v-if="!cell.ship")
            td {{ship}}
            td(v-for="horizontal in [true,false]" )
              q-btn(@click="onAddShip({...cell, horizontal, ship})" :icon="horizontal ? 'mdi-arrow-right':'mdi-arrow-down'" )
      q-btn(@click="onClearField(cell)") Clear

</template>

<style scoped>

</style>