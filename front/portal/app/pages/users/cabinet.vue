<script setup lang="ts">
const tab = ref('posts')
const splitter = ref(20)
</script>

<template lang="pug">
  q-tabs(v-model="tab")
    q-tab(name="posts" label="Posts" )
    q-tab(name="options" label="Options" )
    q-tab(name="password" label="Password" )

  q-tab-panels(v-model="tab" animated swipeable )
    q-tab-panel(name="posts")
      cabinet-posts
    q-tab-panel(name="password")
      cabinet-password
    q-tab-panel(name="options")
      cabinet-options
</template>

<style scoped>

</style>
