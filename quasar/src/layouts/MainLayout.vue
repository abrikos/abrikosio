<template lang="pug">
  q-layout( view="lHh Lpr lFf")
    q-header( elevated)
      q-toolbar
        q-btn( flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" )

        q-toolbar-title Quasar App
        q-btn(to="/xxx") Home
        q-btn(to="/blog") Blog
        q-btn(@click="userStore.logout" v-if="userStore.user") Sign out
        div( v-else)
          q-btn(to="/login") Sign in
          q-btn(to="/signup") Sign up
        div {{userStore.user?.email}}

    q-drawer(v-model="leftDrawerOpen" show-if-above bordered)
      q-list
        q-item-label( header) Drawer

        EssentialLink( v-for="link in linksList" :key="link.title" v-bind="link" )

    q-page-container
      router-view
    q-footer
      q-toolbar
        div Quasar v{{ $q.version }}
</template>

<script setup lang="ts">
import { ref } from 'vue';
import EssentialLink, { type EssentialLinkProps } from 'components/EssentialLink.vue';
import {useAuthStore} from "stores/auth-store";
const userStore = useAuthStore()
async function logout(){

}
const linksList: EssentialLinkProps[] = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev',
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework',
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev',
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev',
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev',
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev',
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev',
  },
];

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
