<template lang="pug">
  q-layout( view="hHh Lpr lff")
    q-header( elevated)
      q-toolbar
        q-btn( flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" )

        q-toolbar-title Quasar App

    q-drawer(v-model="leftDrawerOpen" bordered side="right")
      q-list
        q-item-label( header) Menu
        q-item(v-for="link in linksList" clickable tag="a"  :to="link.link")
          q-item-section(avatar)
            q-icon(:name="link.icon")
          q-item-section
            q-item-label {{ link.title }}
            q-item-label( caption) {{ link.caption }}
        q-item(v-if="userStore.user?.is_staff" to="/post-edit")
          q-item-section(avatar)
            q-icon(name="edit")
          q-item-section
            q-item-label Add post
        div(v-if="userStore.user")
          q-btn(@click="userStore.logout"  flat) Sign out
          q-btn(to="/cabinet" flat) {{userStore.user?.email}}
        div( v-else)
          q-btn(to="/login" flat) Sign in
          q-btn(to="/signup" flat) Sign up

    q-page-container
      router-view
    //q-footer
      q-toolbar
        div Quasar v{{ $q.version }}
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useAuthStore } from 'stores/auth-store';

const userStore = useAuthStore();

async function logout() {}

const linksList = [
  {
    title: 'Home',
    caption: '',
    icon: 'code',
    link: '/',
  },
  {
    title: 'Blog',
    caption: 'view posts',
    icon: 'school',
    link: '/blog',
  },

];


const leftDrawerOpen = ref(true);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
