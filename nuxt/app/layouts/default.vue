<script setup lang="ts">
import {storeToRefs} from 'pinia'; // import storeToRefs helper hook from pinia
import {useCustomStore} from '~/store/custom-store';
import {useCookie} from "#app";

const config = useAppConfig()
const route = useRoute()
const {logUserOut} = useCustomStore(); // use authenticateUser action from  auth store
const {loggedUser, loading} = storeToRefs(useCustomStore())
const themeWidth = useCookie<string>('themeWidth');
const drawerSide = useCookie<string>('drawerSide');
const leftDrawerOpen = ref(true);
const pages = ref()

const pagesUser = [
  {to: '/', label: 'Начало', icon: 'mdi-text-account'},
]
const pagesAdmin = [
  {to: '/admin/post-edit', label: 'Add post', icon: 'mdi-text-account'},
  {to: '/admin/user-list', label: 'Список пользователей', icon: 'mdi-text-account'},
]
const version = ref()
onMounted(()=>{
  useNuxtApp().$GET('/git-commit').then((res)=>{
    version.value = res;
  })
  pages.value = [
    {to: '/blog', label: 'Blog', icon: 'mdi-nas'},
  ]
})

async function clearBase(){
  if(!window.confirm('Clear base?')) return
  await useNuxtApp().$PUT('/admin/clear/base')
  navigateTo('/admin/import')
}

</script>

<template lang="pug">
  q-layout(view="hHh Lpr lff")
    q-header
      q-linear-progress#progress(color="orange" indeterminate v-if="loading" )
      q-toolbar
        q-toolbar-title.cursor-pointer(@click="navigateTo('/')") Blog abrikos
        q-space
        //q-btn(v-for="page in pagesUser" :to="page.to" :label="page.label")
        q-btn(v-for="page in pagesAdmin" :to="page.to" :label="page.label" v-if="loggedUser?.isAdmin")
        q-space
        q-btn.flex.la-align-center(flat dense no-caps v-if="loggedUser" to="/user/cabinet") {{loggedUser.email}}
        q-btn(v-if="loggedUser" @click="logUserOut" icon="mdi-logout" )
        q-btn(v-if="!loggedUser" to="/user/login" icon="mdi-login" )
        //ThemeSwitch
    q-page-container(:class="themeWidth?'page-wrapper':''" )
      q-page
        slot
    q-footer
      small.text-caption(v-if="loggedUser?.isAdmin")
        div Last update: {{version}}



</template>

<style scoped lang="sass">
.page-wrapper
  max-width: 1600px
  margin: auto
#progress
  position: absolute
  height: 10px
  z-index: 100000000
</style>
