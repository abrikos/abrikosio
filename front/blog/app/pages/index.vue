<script setup lang="ts">

const posts = ref([])
async function load(){
  posts.value = await useNuxtApp().$GET('/posts')
}

onMounted(load)
</script>

<template lang="pug">
div.flex
  div(v-for="post of posts")
    post-card(:post="post")
</template>

<style scoped lang="sass">
</style>