<script setup lang="ts">
import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';
import axios from 'src/plugins/axios';
import { useAuthStore } from 'stores/auth-store';

const userStore = useAuthStore();
const route = useRoute();
const post = ref({});
onMounted(async ()=>{
  if(!route.params.id) return
  const res = await axios.get(`/post/${route.params.id}`)
  post.value = res.data
})

</script>

<template lang="pug">
h1 {{ post.title }}
strong {{ post.short }}
div {{ post.body }}
</template>

<style scoped>

</style>
