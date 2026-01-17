<script setup lang="ts">
interface Props {
  user: object;
}
const props = withDefaults(defineProps<Props>(), {
  user: () => ({}),
});
</script>

<template lang="pug">
  q-avatar
    q-img(:src="props.user.avatar || '/static/no-avatar.png'" fit="fill")
    q-tooltip {{props.user.display_name}}

</template>

<style scoped>

</style>
