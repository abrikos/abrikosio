<script setup lang="ts">
import noAvatar from '~~/public/no-avatar.png'
interface Props {
  user?: object;
}
const {user} = defineProps<Props>()
const avatar = computed(() => {
  return user?.avatar ? user.avatar : noAvatar
})

</script>

<template lang="pug">
  span zzz
  q-avatar(v-if="user" square)
    img(:src="avatar")
    q-tooltip {{user?.nickname}}
</template>

<style scoped lang="sass">
img
  border: 1px solid silver
  max-height: 100px
  object-fit: fill
</style>
