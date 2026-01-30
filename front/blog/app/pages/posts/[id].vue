<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

function  setHeaders() {
  useHead({
    title: post.value.title,
    meta: [
      {name: 'description', content: post.value.short},
      {property: 'og:title', content: post.value.title},
      {property: 'og:image', content: post.value.poster},
      {property: 'og:type', content: 'article'},
      {property: 'og:description', content: post.value.short},
    ],
    bodyAttrs: {
      class: 'test',
    },
    script: [{innerHTML: 'console.log(\'Hello world\')'}],
  })
}

const {loggedUser} = useCustomStore()
const post = ref()
const route = useRoute()
const rate = ref(0)
async function load() {
  post.value = await useNuxtApp().$GET('/posts/' + route.params.id)
  if(post.value.errors){
    post.value=null
    return navigateTo('/')
  }
  rate.value = post.value.rate
  //setHeaders()
}

const submitRate = async () => {
  await useNuxtApp().$POST('/posts/rate', {value: rate.value, post_id: post.value.id})
  await load()
}

onMounted(load)
</script>

<template lang="pug">
  div(v-if="post")
    q-bar(dense)
      q-btn(size="sm" icon="mdi-pencil" v-if="loggedUser?.id === post.user.id" :to="`/posts/edit/${post.id}`" flat)
      q-space
      q-rating(v-model="rate" @click="submitRate" max="5" icon="mdi-star-outline" color="red" size="sm" icon-selected="mdi-star"  icon-half="mdi-star-half-full")
      q-space
      span {{post.date}}
    post-view(:post="post" v-if="post")
</template>

<style scoped>

</style>