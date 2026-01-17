<script setup lang="ts">
interface Props {
  user: object;
}
const props = withDefaults(defineProps<Props>(), {
  user: () => ({}),
});
</script>

<template lang="pug">
  q-avatar(size="150px")
    q-img(:src="props.user.avatar || '/static/no-avatar.png'")

</template>

<style scoped>

</style>
