<script setup lang="ts">
const {params} = useRoute()
const data = await useNuxtApp().$POST(`/users/process-restore-password`, params)
</script>

<template lang="pug">
  Banner(color="success") Новый пароль отправлен на указанный e-mail
</template>

<style scoped>

</style>
