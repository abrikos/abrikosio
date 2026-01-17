<script setup lang="ts">
import { ref } from 'vue';
import type { ICredentials } from 'pages/LoginPage.vue';
import axios from '../plugins/axios';
import { useAuthStore } from 'stores/auth-store';
import { useQuasar } from 'quasar';
import PasswordConfirmation from 'components/PasswordConfirmation.vue';
import UserAvatar from 'components/UserAvatar.vue';

const $q = useQuasar();
const userStore = useAuthStore();
const credentials = ref<ICredentials>({ password: '', password2: '' });
const errors = ref({});

async function updateUser(deleteAvatar:boolean) {
  if (!userStore.user) return;
  if(deleteAvatar){
    userStore.user.avatar = null;
  }
  const res = await axios.patch(`/user/${userStore.user.id}/`, userStore.user);
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

    q-form(@submit="updateUser()")
      q-input(v-model="userStore.user.first_name" label="First Name" )
      q-input(v-model="userStore.user.last_name" label="Last Name" )
      q-file
      q-btn(type="submit") Save

    user-avatar(:user="userStore.user")
    q-btn(@click="updateUser(true)") Delete
    q-uploader(url="" @added="setAvatar")

</template>

<style scoped></style>
