<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import {RouterLink, RouterView} from "vue-router";


</script>

<template lang="pug">
nav
  RouterLink(to="/") Home
  RouterLink(to="/blog") Blog
main
  RouterView
</template>

<style scoped>

</style>
