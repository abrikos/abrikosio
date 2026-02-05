<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const {loggedUser} = storeToRefs(useCustomStore())
const credentials = ref({})
const errors = ref({})
const $q = useQuasar()
async function setPassword() {
  if (!loggedUser.value) return;
  const res = await useNuxtApp().$PATCH(`/users/${loggedUser.value.id}/password`, credentials.value);
  if(!res?.error) {
    $q.notify({message: 'Password changed', color: 'green'});
  }else{
    errors.value = res.error
  }
}

</script>

<template lang="pug">
q-card
  q-form(@submit="setPassword")
    q-card-section
      password-confirmation(v-model="credentials" :errors="errors")
    q-card-actions
      q-btn(type="submit" color="primary" ) Set new password

</template>

<style scoped>

</style>