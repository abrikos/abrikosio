<script setup lang="ts">
import {useCustomStore, type UserPayloadInterface} from '~/store/custom-store';
import {useQuasar} from 'quasar'

const {signup} = useCustomStore()

const newUser = import.meta.env.DEV ? {email: Math.random() + '@google.com', password: '1'} : {}
const user = ref<UserPayloadInterface>(newUser)
const errors = ref({})

async function submit() {
    //if (await form.value.validate()) {
    const res = await signup(user.value)
    if (res?.errors) {
      console.log(res)
      errors.value = res.errors
      //navigateTo('/users/cabinet')
    }
}

</script>

<template lang="pug">
  q-form.fixed-center(v-if="user" @submit="submit")
    q-card.q-ma-sm(style="width:400px")
      q-card-section
        div.h1 Регистрация
      q-card-section
        q-input(v-model="user.email" label="email" :rules="$email" type="email")
        password-confirmation(v-model="user" :errors="errors")
      q-card-actions
        q-btn(type="submit" label="Отправить" )
        //q-btn(@click="test" label="test" )

</template>

<style scoped>

</style>
