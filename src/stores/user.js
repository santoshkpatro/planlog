import { defineStore } from 'pinia'
import { http } from '@/api/v1'

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    user: null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.user,
  },
  actions: {
    setLoggedInUser(user) {
      this.user = user
      const { access_token } = user
      http.defaults.headers.common['Authorization'] = `Bearer ${access_token}`
      localStorage.setItem('user', JSON.stringify(user))
    },
    removeLoggedInUser() {
      this.user = null
      localStorage.removeItem('user')
      location.reload()
    },
  },
})
