<script setup lang="ts">
import MarkdownIt from 'markdown-it';
import { computed } from 'vue';

const {text} = defineProps<{ text?: string }>()

const md = new MarkdownIt();

const renderedMarkdown = computed(() => {
  if (text) {
    return md.render(text);
  }
});
</script>

<template lang="pug">
  div(v-html="renderedMarkdown" )
</template>

<style scoped></style>
