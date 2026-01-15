<script setup>
import { ref, computed, onMounted } from "vue";
const data = ref(1)
function add(){
  const formData = new FormData();
  formData.append('title',data.value);
  fetch("/api/post/",{method:"POST",body:formData})
}
</script>

<template lang="pug">
div Bubu
  input(v-model="data")
  button(@click="add") send
</template>

<style scoped>

</style>