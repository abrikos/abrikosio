<script setup lang="ts">
import {useCustomStore} from '~/store/custom-store';

const {loggedUser, login} = useCustomStore()
const config = useRuntimeConfig()
const $q = useQuasar()
const user = ref(config.app.buildId==='dev' ? {email: 'abrikoz@gmail.com', password: '1'}:{email: '', password: ''})
const error = ref()
async function submit() {
  error.value = await login(user.value)
}
onMounted(()=>{
  if(loggedUser) {navigateTo('/users/cabinet')}
})

function reset() {
  user.value = {email: '', password: ''}
}
</script>

<template lang="pug">
q-card.q-pa-sm
  q-toolbar
    q-toolbar-title Вход
  q-form(@submit="submit" @reset="reset")
    q-input(v-model="user.email" label="Логин")
    br
    q-input(v-model="user.password" label="Пароль" type="password" )
    q-card-section.text-center
      q-btn.full-width(type="submit" label="Вход" color="primary" :flat="false")
    q-card-section
      div
        router-link(to="/users/registration") Зарегистрироваться
      div
        router-link(to="/users/password-restore") Восстановить пароль
    q-card-section.text-red {{error?.error}}
</template>

<style scoped>

</style>
