import axios from 'axios'

export const http = axios.create({
  baseURL:
    import.meta.VITE_BACKEND_BASE_V1_API || 'http://127.0.0.1:8000/api/v1',
})

export const verifyConfirmationToken = (confirmationToken) =>
  http.get('/user/register/', {
    params: { confirmation_token: confirmationToken },
  })

export const verifyUserAvailablity = (data) =>
  http.get('/user/availability', {
    params: {
      ...data,
    },
  })

export const registerUser = (data, confirmationToken) => {
  http.post('/user/register/', data, {
    params: {
      confirmation_token: confirmationToken,
    },
  })
}

export const sendConfirmationEmail = (email) => {
  http.get('/user/register/', {
    params: {
      send_confirmation: email,
    },
  })
}

export const loginUser = (data) => http.post('/user/login/', data)

export const userProfile = () => http.get('/user/profile/')
