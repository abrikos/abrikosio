<script setup lang="ts">

const {post} = defineProps<{ post: object }>()

</script>

<template lang="pug">
div.q-pa-lg
  h1 {{ post.title }}
  div.bg-grey-4.q-pa-sm
    img.poster(:src="post.poster" v-if="post.poster")
    strong {{post.short}}
  mark-down(:text="post.body")
  //p.body(v-html="post.markdown_body")
</template>

<style scoped lang="sass">
img
  max-width: 300px
  max-height: 300px
img.poster
  float: right
video
  border: 1px solid red
  width: 300px
  height: 300px
</style>
