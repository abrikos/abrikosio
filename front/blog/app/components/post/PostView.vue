<script setup lang="ts">

import MarkDown from "~/components/cabinet/MarkDown.vue";

const {post} = defineProps<{ post: object }>()

</script>

<template lang="pug">
div.q-pa-lg
  h1 {{ post.title }}
  div.bg-grey-4.q-pa-sm.flex
    div.q-mx-sm(v-if="post.poster")
      img.poster(:src="post.poster")
    strong {{post.short}}
  mark-down#mark-down(:text="post.body")
  //p.body(v-html="post.markdown_body")
</template>

<style scoped lang="sass">
img
  max-width: 300px
  max-height: 300px
//img.poster
//  float: right
video
  border: 1px solid red
  width: 300px
  height: 300px
</style>
