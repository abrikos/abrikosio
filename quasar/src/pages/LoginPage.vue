<script setup lang="ts">
import {ref} from 'vue'
import { Cookies } from 'quasar'
import axios from "axios";


const user = ref({email:'test211@b.com',password:'1'})

async function login(){
  const csrftoken =  Cookies.get('csrftoken')
  const token =  await axios.post('/token/', user.value, {headers: {'CSRFToken': csrftoken}})
  const users = await  axios.get('/user', {headers: {'Authorization': 'Bearer ' + token.data.access}})
  console.log(users)
  Cookies.set('auth', token.data.access)
}
</script>

<template lang="pug">
q-page
  q-input(v-model="user.email")
  q-input(v-model="user.password")
  q-btn(@click="login") Send
</template>

<style scoped>

</style>
