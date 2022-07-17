<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  verifyConfirmationToken,
  verifyUserAvailability,
  registerUser,
  sendConfirmationEmail,
} from '@/api/v1'

const router = useRouter()
const route = useRoute()

const token = ref('')
const newEmail = ref('')
const formGroup = reactive({
  full_name: '',
  email: '',
  username: '',
  password: '',
})
const isUsernameAvailable = ref(false)

onMounted(async () => {
  const { confirmation_token } = route.query
  token.value = confirmation_token

  if (confirmation_token) {
    try {
      const { data } = await verifyConfirmationToken(token.value)
      formGroup.email = data.data.email
    } catch (e) {
      console.log(e)
    }
  }
})

function checkForValidUsername(e) {
  setTimeout(async () => {
    if (e.target.value) {
      try {
        const { data } = await verifyUserAvailability({
          username: e.target.value,
        })
        isUsernameAvailable.value = data.detail
      } catch (e) {
        console.log(e)
      }
    }
  }, 300)
}

async function handleForm() {
  try {
    const { data } = await registerUser(formGroup, token.value)
    console.log(data.detail)
  } catch (e) {
    console.log(e)
  }
}

async function handleConfirmationEmail() {
  try {
    const { data } = await sendConfirmationEmail(newEmail.value)
  } catch (e) {
    console.log(e)
  }
}
</script>

<template>
  <div class="container">
    <div v-if="token">
      <h1>Complete registration</h1>
      <form @submit.prevent="handleForm">
        <div class="mb-2">
          <label for="username" class="form-label">Username</label>
          <input
            @keyup="checkForValidUsername"
            type="text"
            class="form-control"
            v-model="formGroup.username"
            id="username"
            :class="{
              'is-valid': isUsernameAvailable,
              'is-invalid': !isUsernameAvailable,
            }"
          />
          <div v-if="isUsernameAvailable" class="valid-feedback">
            Username is available
          </div>
          <div v-if="!isUsernameAvailable" class="invalid-feedback">
            Username is not available
          </div>
        </div>
        <div class="mb-2">
          <label for="email" class="form-label">Email</label>
          <input
            type="email"
            class="form-control"
            v-model="formGroup.email"
            id="email"
            disabled="true"
          />
        </div>
        <div class="mb-2">
          <label for="full_name" class="form-label">Full Name</label>
          <input
            type="text"
            class="form-control"
            v-model="formGroup.full_name"
            id="full_name"
          />
        </div>
        <div class="mb-2">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            class="form-control"
            v-model="formGroup.password"
            id="password"
          />
        </div>
        <button class="btn btn-success" type="submit">Register</button>
      </form>
    </div>
    <div v-else>
      <h1>Enter your email address</h1>
      <form @submit.prevent="handleConfirmationEmail">
        <div class="mb-2">
          <label for="email" class="form-label">Email</label>
          <input
            type="email"
            class="form-control"
            v-model="newEmail"
            id="email"
            required
          />
        </div>

        <button class="btn btn-sm btn-primary" type="submit">
          Send registration link
        </button>
      </form>
    </div>
  </div>
</template>
