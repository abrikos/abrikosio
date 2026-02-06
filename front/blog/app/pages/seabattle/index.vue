<script setup lang="ts">
import SeaBattlePlay from "~/components/seabattle/Sea-Battle-Play.vue";
import SeaBattleList from "~/components/seabattle/Sea-Battle-List.vue";

const route = useRoute()
</script>

<template lang="pug">
  sea-battle-play(v-if="route.query.id")
  sea-battle-list(v-else)

</template>

<style scoped>

</style>