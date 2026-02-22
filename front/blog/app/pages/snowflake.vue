<script setup lang="ts">

const width = 400
const height = 400
const lines = [0, 1, 2, 3, 4, 5]

const triangle = computed(() => {
  return `${xTriangle.value},0 ${xTriangle.value * 3},${-yTriangle.value} ${xTriangle.value * 3},${yTriangle.value}`
})

const xTriangle = ref(0)
const yTriangle = ref(0)

function randomize() {
  const max = 50
  const min = 5
  if (Math.random() < 0.5) {
    xTriangle.value = Math.random() * (max - min) + min
    yTriangle.value = Math.random() * (max - min) + min
  }else{
    xTriangle.value = yTriangle.value = 0
  }

}

randomize()

</script>

<template lang="pug">
  svg(
    @click="randomize"
    xmlns="http://www.w3.org/2000/svg"
    :viewBox="`-${width/2} -${height/2} ${width} ${height}`"
    :width="width"
    :height="height"
    aria-labelledby="scissors"
    role="presentation")
    title(
      id="scissors"
      lang="en") Scissors Animated Icon
    path(
      id="bk"
      fill="#fff"
      d="M0 0h100v100H0z")
    g(ref="leftscissor" :transform="`rotate(${60*i})`" v-for="i in lines" )
      line(x1="0", y1="0", x2="100", y2="0" stroke="black")
      circle(cx="100", cy="0", r="10")
      polygon(:points="triangle")
  q-btn(@click="randomize") Randomize
</template>

<style scoped>

</style>