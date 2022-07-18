<script setup>
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { loginUser } from '@/api/v1'

const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

const isLoading = ref(false)
const form = reactive({
  username: '',
  password: '',
})

async function handleSubmit() {
  try {
    isLoading.value = true

    const { data } = await loginUser(form)

    userStore.setLoggedInUser(data)

    if(route.query.redirect) {
      router.push(route.query.redirect)
      return
    }

    router.push({ name: 'profile' })
  } catch (e) {
    console.log(e)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="flex h-screen justify-center items-center">
    <!-- ⬅️ THIS DIV WILL BE CENTERED -->
    <form
      @submit.prevent="handleSubmit"
      class="bg-white drop-shadow-2xl rounded px-8 pt-6 pb-8 mb-4"
    >
      <h1 class="text-3xl mb-5">Login</h1>
      <div class="mb-4">
        <label
          class="block text-gray-700 text-sm font-bold mb-2"
          for="username"
        >
          Username or Email
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="username"
          type="text"
          placeholder=""
          v-model="form.username"
        />
      </div>
      <div class="mb-6">
        <label
          class="block text-gray-700 text-sm font-bold mb-2"
          for="password"
        >
          Password
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
          id="password"
          type="password"
          placeholder="******************"
          v-model="form.password"
        />
        <!-- <p class="text-red-500 text-xs italic">Please choose a password.</p> -->
      </div>
      <div class="flex items-center justify-between">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline flex"
          type="submit"
          :disabled="isLoading"
        >
          <svg
            class="animate-spin h-5 w-5 mr-3"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            v-if="isLoading"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          <p>Login</p>
        </button>
        <a
          class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
          href="#"
        >
          Forgot Password?
        </a>
      </div>
    </form>
  </div>
</template>
