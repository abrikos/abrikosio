<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const route = useRoute()
const {$event} = useNuxtApp()
const {loggedUser} = storeToRefs(useCustomStore())
const {getMe} = useCustomStore()
const $q = useQuasar()
async function updateUser() {
  if (!loggedUser.value) return;
  const res = await useNuxtApp().$PATCH(`/users/${loggedUser.value.id}/`, loggedUser.value);
  if(!res.error) {
    $q.notify({message: 'Success', color: 'green'});
  }
}

</script>

<template lang="pug">
div(v-if="loggedUser")
  q-card.q-mb-lg
    q-card-section
      q-form(@submit="updateUser()")
        q-input(v-model="loggedUser.nickname" label="Nick Name" )
        q-input(v-model="loggedUser.avatar" label="Avatar" )
          template(v-slot:after)
            user-avatar(:user="loggedUser")

        q-card-actions(@submit="updateUser()")
          q-btn(type="submit" color="primary" ) Save

  //q-card
    q-card-section
      q-file(@update:model-value="setAvatar" label="Choose avatar" outlined counter)
        template(v-slot:append)

        template(v-slot:before)
          user-avatar(:user="loggedUser")
          q-btn(@click="deleteAvatar" icon="mdi-delete" color="red" )
</template>

<style scoped>

</style>