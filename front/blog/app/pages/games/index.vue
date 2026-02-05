<script setup lang="ts">

import SeaBattleClient from "~/components/games/seabattle/SeaBattleClient.vue";
import SeaBattleOpponent from "~/components/games/seabattle/Sea-Battle-Opponent.vue";
</script>

<template lang="pug">
div.row
  div.col
    SeaBattleClient
  div.col
    sea-battle-opponent
</template>

<style scoped>

</style>