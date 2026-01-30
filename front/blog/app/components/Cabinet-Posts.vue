<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const {$listen} = useNuxtApp()
const posts = ref([])
const load = async()=>{
  posts.value = await useNuxtApp().$GET('/posts/user_posts')
}
onMounted(load)
$listen('posts-load', load)
</script>

<template lang="pug">
  div.flex.justify-between
    div(v-for="post of posts")
      post-card(:post="post" :cabinet="true")

</template>

<style scoped>

</style>