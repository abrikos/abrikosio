<script setup lang="ts">
import { ref } from 'vue';
import type { ICredentials } from 'pages/LoginPage.vue';
import axios from '../plugins/axios';
import { useAuthStore } from 'stores/auth-store';
import { useQuasar } from 'quasar';
import PasswordConfirmation from 'components/PasswordConfirmation.vue';

const $q = useQuasar();
const userStore = useAuthStore();
const credentials = ref<ICredentials>({ password: '', password2: '' });
const errors = ref({});

async function setPassword() {
  if (!userStore.user) return;
  const res = await axios.put(`/user/${userStore.user.id}/set_password/`, credentials.value);
  if (res.data.error) {
    errors.value = res.data.error;
  }
  $q.notify({ message: res.data.status, color: 'green' });
}

async function setAvatar(file: string) {
  if (!userStore.user) return;
  const res = await axios.post(`/user/${userStore.user.id}/set_avatar/`, file, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  $q.notify({ message: res.data.status, color: 'green' });
}
</script>

<template lang="pug">
  q-page
    q-toolbar
      q-toolbar-title Cabinet
    q-form(@submit="setPassword")
      password-confirmation(v-model="credentials" :errors="errors")
      q-btn(type="submit") Save
    div {{userStore.user.avatar}}
    q-img(:src="userStore.user.avatar")
    q-uploader(url="" @added="setAvatar")


</template>

<style scoped></style>
