<script setup>
import { ref, onMounted } from 'vue'
import { getBoards } from '@/api/v1'

const boards = ref([])

onMounted(async () => {
  try {
    const { data } = await getBoards()
    boards.value = data
  } catch (e) {
    console.log(e)
  }
})
</script>

<template></template>
