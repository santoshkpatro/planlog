<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import Navbar from '@/components/Navbar.vue'
import BoardList from '@/components/BoardList.vue'

const route = useRoute()

onMounted(() => {
  console.log(window.location.host.split('.')[0])
})
</script>

<template>
  <Navbar />
  <BoardList />
</template>
