<template lang="pug">
  q-page.row.items-center.justify-evenly
    q-card(v-for="post in posts")
      q-toolbar
        q-toolbar-title
          q-avatar
            user-avatar(:user="post.user")
          q-btn(:to="`/post-view/${post.id}`" flat no-caps) {{ post.title }}
      q-card-section {{ post.short }}
        small {{ post.created_at }}
      q-card-actions
        q-btn(size="sm" icon="edit" v-if="userStore.user?.id === post.user.id" :to="`/post-edit/${post.id}`")
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import type { Todo, Meta } from 'components/models';
import ExampleComponent from 'components/ExampleComponent.vue';
import axios from 'src/plugins/axios';
import UserAvatar from 'components/UserAvatar.vue';
import { useAuthStore } from 'stores/auth-store';

const userStore = useAuthStore();
const posts = ref([]);
onMounted(async () => {
  const res = await axios.get(`/post/`);
  posts.value = res.data;
});
</script>
