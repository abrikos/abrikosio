<script setup lang="ts">
import { ref } from 'vue';
import type { ICredentials } from 'pages/LoginPage.vue';
import { useAuthStore } from 'stores/auth-store';
import validator from '../plugins/validators';
import PasswordConfirmation from 'components/PasswordConfirmation.vue';
const errors = ref({});

const credentials = ref<ICredentials>({ email: Math.random() + '@gg.com', password: '1' });

async function signup() {
  const auth = useAuthStore();
  const res = await auth.signup(credentials.value);
  if (res.data.error) {
    errors.value = res.data.error;
  }
}
</script>

<template lang="pug">
  q-form(@submit="signup")
    q-input(v-model="credentials.email" label="Email" type="email" :rules="validator.email" :error="!!errors.email" :error-message="errors.email?.join()")
    password-confirmation(v-model="credentials" :errors="errors")
    q-btn(type="submit") Sign up
</template>

<style scoped></style>
