<template lang="pug">
  q-layout( view="hHh Lpr lff")
    q-header( elevated)
      q-linear-progress#progress(color="orange" indeterminate v-if="loading" )
      q-toolbar
        q-btn( flat dense round icon="mdi-menu" aria-label="Menu" @click="toggleLeftDrawer" )

        q-toolbar-title и.о. Абрикос222

    q-drawer(v-model="leftDrawerOpen" bordered side="left")
      q-list
        q-item(v-for="link in menuItems.filter(i=>i.show)" clickable tag="a"  :to="link.link")
          q-item-section(avatar)
            q-icon(:name="link.icon" color="blue" )
          q-item-section
            q-item-label {{ link.title }}
            q-item-label( caption) {{ link.caption }}
        q-item(v-if="loggedUser" clickable tag="a"  to="/users/cabinet")
          q-item-section(avatar)
            user-avatar(:user="loggedUser")
          q-item-section
            q-item-label {{ loggedUser.nickname }}
            q-item-label( caption) Cabinet
      div(v-if="loggedUser?.is_admin")
        div {{git}}
    q-page-container
      slot
    //q-footer
      q-toolbar
        div Quasar v{{ $q.version }}
</template>
<style lang="sass">
#progress
  position: absolute
  height: 10px
  z-index: 100000000

</style>

<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const router = useRouter();
const {loggedUser, loading} = storeToRefs(useCustomStore())
const git = ref({})
onMounted(()=>{
  useNuxtApp().$GET('/git').then(res=>{
    console.log(res)
    git.value = res
  })
})
const menuItems = computed(() => {
  return [
    {
      title: 'Home',
      caption: '',
      icon: 'mdi-home',
      link: '/',
      show: true
    },
    {
      title: 'Sign out',
      caption: '',
      icon: 'mdi-logout',
      link: '/users/logout',
      show: loggedUser.value
    },
    {
      title: 'Login',
      caption: '',
      icon: 'mdi-login',
      link: '/users/login',
      show: !loggedUser.value
    },{
      title: 'Registration',
      caption: '',
      icon: 'mdi-login',
      link: '/users/registration',
      show: !loggedUser.value
    }
  ]



})



const leftDrawerOpen = ref(true);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
