<script setup lang="ts">
import axios from 'src/plugins/axios';
import { useAuthStore } from 'stores/auth-store';
import { useQuasar } from 'quasar';
import { computed, onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();
const newPost = computed(() => !route.params.id);
const userStore = useAuthStore();
const $q = useQuasar();
const post = ref({});

onMounted(async ()=>{
  if(!route.params.id) return
  const res = await axios.get(`/post/${route.params.id}`)
  post.value = res.data
})

async function onSubmit() {
  if (!userStore.user) return;
  console.log(newPost.value, )
  const res = newPost.value
    ? await axios.post(`/post/`, post.value)
    : await axios.patch(`/post/${route.params.id}/`, post.value);
  if (res.status < 400) {
    $q.notify({ message: 'Success', color: 'green' });
    if (newPost.value) {
      await router.push('/post-edit/1');
    }
  }
}
</script>

<template lang="pug">
q-form(@submit="onSubmit")
  q-input(v-model="post.title" label="Title")
  q-input(v-model="post.short" label="Short" type="textarea")
  q-input(v-model="post.body" label="Body" type="textarea")
  q-toggle( v-model="post.published" label="Published")
  div {{ post.created_at  }}
  q-btn(type="submit") Save
</template>

<style scoped></style>
