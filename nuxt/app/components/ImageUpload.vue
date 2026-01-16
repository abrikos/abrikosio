<script setup lang="ts">
import DeleteButton from "~/components/DeleteButton.vue";

const {$listen, $event} = useNuxtApp()
const pictures = ref([])
const files = ref()

$listen('picture:delete', load)

async function load() {
  pictures.value = await useNuxtApp().$GET('/blog/pictures') as never[]
}


function insertPicture(picture: string) {
  const html = `<img src='/api/blog/picture/${picture}' alt='${picture}' class="picture">`
  $event('picture:insert', html)
}

async function upload(files: any) {

  const formData = new FormData();
  for(const file of files) {
    formData.append('files[]', file)
  }
  await useNuxtApp().$POST('/blog/upload', formData)
  await load()
}

onMounted(load)

</script>

<template lang="pug">
  q-card(style="width: 100%")
    q-toolbar
      q-file(multiple v-model="files" label="Upload" @update:model-value="upload" outlined)
      q-space
      q-btn(icon="mdi-close" @click="()=>$event('dialog:close')")
    q-card-section.scroll(style="max-height: 50vh")
      div.pictures
        div.pic-wrapper(v-for="picture in pictures")
          div.picture
            img(:src="`/api/blog/picture/${picture}`")
            q-tooltip {{picture}}
          div.tools.text-right
            q-btn(icon="mdi-image" @click="insertPicture(picture)")
            DeleteButton(:name="picture" :path="`/blog/picture`" :id="picture" event="picture:delete")
</template>

<style scoped lang="sass">
$picture-size: 130px
.uploader ::v-deep(.q-field__control)
  height: 80px

.pictures
  display: flex
  flex-wrap: wrap

  .pic-wrapper
    border: 1px solid silver
    margin: 5px
    background-color: silver

  .picture
    background-color: white
    width: $picture-size
    height: $picture-size
    //border: 1px solid silver
    display: flex
    align-items: center
    justify-content: center
    margin: 1px

    img
      border: solid 1px silver
      max-width: $picture-size - 2px
      max-height: $picture-size - 2px
</style>