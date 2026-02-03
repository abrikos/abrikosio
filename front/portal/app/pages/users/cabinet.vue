<script setup lang="ts">
const tab = ref('receipts')
const splitter = ref(20)
</script>

<template lang="pug">
  q-tabs(v-model="tab")
    q-tab(name="receipts" label="Чеки" )
    q-tab(name="options" label="Options" )
    q-tab(name="password" label="Password" )

  q-tab-panels(v-model="tab" animated swipeable )
    q-tab-panel(name="receipts")
      cabinet-reciepts
    q-tab-panel(name="password")
      cabinet-password
    q-tab-panel(name="options")
      cabinet-options
</template>

<style scoped>

</style>
