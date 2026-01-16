<script setup lang="ts">
const code = ref()

async function send() {
  const res = await useNuxtApp().$GET('/user/registration-code/' + code.value)
  if (res) navigateTo('/')
}
</script>

<template lang="pug">
  q-card.fixed-center
    q-toolbar
      q-toolbar-title Регистрация
    q-card-section
      q-banner.bg-green-4 На указанный e-mail выслан код подтверждения
      q-input(v-model="code" )
      q-btn(@click="send") Отправить

</template>

<style scoped>

</style>