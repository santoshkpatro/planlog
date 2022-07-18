<script setup>
import Navbar from '@/components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { getBoards } from '@/api/v1'

const boards = ref([])

async function fetchBoards() {
  try {
    const { data } = await getBoards()
    boards.value = data
  } catch (e) {
    console.log(e)
  }
}

onMounted(() => {
  fetchBoards()
})
</script>

<template>
  <Navbar />
</template>
