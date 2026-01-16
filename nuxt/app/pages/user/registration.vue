<script setup lang="ts">
import {useCustomStore} from '~/store/custom-store';
import UserForm from "~/components/UserForm.vue";
import { useQuasar } from 'quasar'

const {signupUser} = useCustomStore()
const config = useRuntimeConfig()
const testuser ={email: Math.random()+'@google.com', password:'1', password1:'1'}
const user = ref(config.app.buildId==='dev' ? testuser: {})
const form = ref()

const res = ref(true)
async function submit() {
  if(await form.value.validate()) {
    const res = await useNuxtApp().$POST('/user/registration', user.value)
    if(res) {
      navigateTo('/user/registration-done')
    }
  }
}

const toast = useToast()

const $q = useQuasar()

const showToast = () => {

}
async function test() {
  console.log($q)
  $q.notify({
    color: 'info',
    message:'Frrrrrr',
    position: 'top',
  })
  const x = toast.add({
    title: 'fffffffffff',
  })
  console.log(x)
}

</script>

<template lang="pug">
  q-form.fixed-center(v-if="user" ref="form" @submit="submit")
    q-card.q-ma-sm(style="width:400px")
      q-card-section
        div.h1 Регистрация
      q-card-section
        UserForm(v-model="user")
      q-card-actions
        q-btn(type="submit" label="Отправить" )
        q-btn(@click="test" label="test" )

</template>

<style scoped>

</style>
