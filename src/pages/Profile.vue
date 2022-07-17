<script setup>
import { reactive, ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { userProfile } from '@/api/v1'

onMounted(async () => {
  try {
    await userProfile()
  } catch (e) {
    console.log(e)
  } finally {
  }
})
</script>

<template>
  <h1>Profile</h1>
</template>
