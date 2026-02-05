<script setup lang="ts">
import {useCustomStore} from "~/store/custom-store";

const route = useRoute()
const $q = useQuasar()
const {loggedUser} = storeToRefs(useCustomStore())
const post = ref({})

async function load() {
  if (!route.params.id) return
  post.value = await useNuxtApp().$GET('/posts/' + route.params.id)
  if (!post.value || !post.value.id) {
    navigateTo('/')
  }
}

watch(()=>route.params.id, (value) => {
  if(!value) {
    post.value = {}
  }
})

onMounted(load)
const errors = ref({})
async function onSubmit() {
  if (!loggedUser.value) return;
  let res
  if (route.params.id) {
    res = await useNuxtApp().$PATCH(`/posts/${route.params.id}`, post.value)
  } else {
    res = await useNuxtApp().$POST(`/posts/`, post.value)
  }
  if (res.id) {
    $q.notify({message: 'Success', color: 'green'});
    if(res.id) {
      navigateTo(`/posts/edit/${res.id}`)
    }
  }else if(res.errors){
    errors.value = res.errors
  }
}

async function onReset() {
  errors.value = {}
  await load()
}

</script>

<template lang="pug">
  div.row.q-gutter-md
    div.col-sm.q-pa-lg
      q-card
        q-form(@submit="onSubmit" @reset="onReset")
          q-card-section
            q-input(v-model="post.title" label="Title" :error="!!errors.title" :error-message="errors.title?.join(',')")
            q-input(v-model="post.poster" label="Poster image url" hint="Place link for any image")
              template(v-slot:prepend)
                q-icon(name="mdi-image")
            q-input(v-model="post.short" label="Short" type="textarea"  filled autogrow  :error="!!errors.short" :error-message="errors.short?.join(',')")


            q-input(v-model="post.body" label="Body (accepts markdown syntax)" type="textarea" filled autogrow)
              template(v-slot:append)

                q-icon(name="mdi-help")
                  q-popup-proxy
                    q-banner
                      a(href="https://skillbox.ru/media/code/yazyk-razmetki-markdown-shpargalka-po-sintaksisu-s-primerami/" target="_blank") Markdown syntax
                q-tooltip Markdown syntax
            div.row.items-center
              div.col
                q-toggle( v-model="post.published" label="Show for all")
              div.col.text-right {{ post.date  }}

          q-card-actions.flex.justify-between
            q-btn(type="submit" color="primary" :flat="false" :label="route.params.id ? 'Save':'Create'")
            q-btn(type="reset" :flat="false" label="Reset" v-if="route.params.id")
    div.col-sm
      router-link(:to="`/posts/${route.params.id}`") View Post
      div.preview
        post-view(:post="post")


</template>

<style scoped lang="sass">
.preview
  border: 1px solid black
  transform: scale(.7)
  transform-origin: top left
  //transition: scale 0.3s ease

</style>