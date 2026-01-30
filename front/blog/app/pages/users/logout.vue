<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const {logout} = useCustomStore();
logout()
navigateTo('/users/login')
</script>

<template>

</template>

<style scoped>

</style>