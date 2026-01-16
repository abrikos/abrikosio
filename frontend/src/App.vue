<script setup>

</script>

<template lang="pug">
nav
  RouterLink(to="/" exact) Home
  RouterLink(to="/blog" exact) Blog
main
  RouterView
</template>

<style scoped>

</style>
