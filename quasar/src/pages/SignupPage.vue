<script setup lang="ts">
import {ref} from 'vue'
import type { ICredentials } from 'pages/LoginPage.vue';
import {useAuthStore} from "stores/auth-store";
import axios from '../plugins/axios';

const credentials = ref<ICredentials>({email:Math.random()+ '@gg.com', password:'1'});
async function signup(){
  const auth = useAuthStore()
  await auth.signup(credentials.value)
}
</script>

<template lang="pug">
q-input(v-model="credentials.email" label="Email" )
q-input(v-model="credentials.password" label="Password" )
q-input(v-model="credentials.password2" label="Password confirm" )
q-btn(@click="signup") Sign up
</template>

<style scoped>

</style>
