<script setup lang="ts">

const posts = ref([])
async function load(){
  posts.value = await useNuxtApp().$GET('/posts')
}

onMounted(load)
</script>

<template lang="pug">
div INDEX
</template>

<style scoped lang="sass">
</style>