<script setup lang="ts">
import {ref} from 'vue'
import {useAuthStore} from "stores/auth-store";
import { useRouter } from 'vue-router';

const router = useRouter();
export interface ICredentials {
  email?: string;
  password?: string;
  password2?: string;
}


const userStore = useAuthStore()
const credentials = ref<ICredentials>({email:'test211@b.com',password:'1'})

async function login(){
  const user = await userStore.login(credentials.value)
  if(user){
    await router.push('/cabinet')
  }
}
</script>

<template lang="pug">
q-page
  q-input(v-model="credentials.email")
  q-input(v-model="credentials.password")
  q-btn(@click="login") Send
</template>

<style scoped>

</style>
