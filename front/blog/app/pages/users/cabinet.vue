<script setup lang="ts">
const route = useRoute()
if(!route.query.tab){
  navigateTo({query:{tab:'receipts'}})
}
</script>

<template lang="pug">
  q-tabs
    q-route-tab(name="posts" label="Posts" :to="{query:{tab:'posts'}}")
    q-route-tab(name="receipts" label="Receipts" :to="{query:{tab:'receipts'}}")
    q-route-tab(name="options" label="Options" :to="{query:{tab:'options'}}")
    q-route-tab(name="password" label="Password" :to="{query:{tab:'password'}}")

  q-tab-panels(v-model="route.query.tab" animated swipeable )
    q-tab-panel(name="posts")
      cabinet-posts
    q-tab-panel(name="receipts")
      cabinet-reciepts
    q-tab-panel(name="options")
      cabinet-options
    q-tab-panel(name="password")
      cabinet-password
</template>

<style scoped>

</style>
