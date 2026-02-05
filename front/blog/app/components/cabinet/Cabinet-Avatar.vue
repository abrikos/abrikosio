<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const {loggedUser} = storeToRefs(useCustomStore())
</script>

<template lang="pug">
  user-avatar(:user="loggedUser")
  q-btn(@click="updateUser(true)") Delete
  q-uploader(url="" @added="setAvatar")

</template>

<style scoped>

</style>