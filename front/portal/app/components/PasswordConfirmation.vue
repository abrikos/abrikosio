<script setup lang="ts">
import { onMounted, ref } from 'vue';

interface Props {
  errors?: object;
}
const errors = ref({});
const props = defineProps<Props>()
const credentials = defineModel()

</script>

<template lang="pug">
  q-input(v-model="credentials.password" label="Password"  :error="!!props.errors.password" :error-message="props.errors.password?.join()")
  q-input(v-model="credentials.password2" label="Password confirm"  :error="!!props.errors.password2" :error-message="props.errors.password2?.join()")
</template>

<style scoped></style>
