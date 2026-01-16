<script setup lang="ts">
import { ref } from 'vue';
import type { ICredentials } from 'pages/LoginPage.vue';
import { useAuthStore } from 'stores/auth-store';
import validator from '../plugins/validators';
import { useRouter } from 'vue-router';
const router = useRouter()
const errors = ref({});

const credentials = ref<ICredentials>({ email: Math.random() + '@gg.com', password: '1' });

async function signup() {
  const auth = useAuthStore();
  const res = await auth.signup(credentials.value);

  if (res.data.error) {
    for(const key in res.data.error) {
      res.data.error[key] = res.data.error[key].join();
    }
    errors.value = res.data.error;
  }else{
    await router.push('/');
  }
}
</script>

<template lang="pug">
  q-form(@submit="signup")
    q-input(v-model="credentials.email" label="Email" type="email" :rules="validator.email" :error="!!errors.email" :error-message="errors.email")
    q-input(v-model="credentials.password" label="Password"  :error="!!errors.password" :error-message="errors.password")
    q-input(v-model="credentials.password2" label="Password confirm"  :error="!!errors.password2" :error-message="errors.password2")
    q-btn(type="submit") Sign up
</template>

<style scoped></style>
