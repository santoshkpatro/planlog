import { defineStore } from 'pinia'
import { http } from '@/api/v1'
import { createAvatar } from '@dicebear/avatars'
import * as initialStyle from '@dicebear/avatars-initials-sprites'

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    user: null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.user,
    profileImage: (state) => {
      if (state.user) {
        if (!state.user.avatar) {
          return createAvatar(initialStyle, {
            seed: state.user.full_name,
            dataUri: true,
            size: 30,
            radius: 50,
          })
        }

        return state.user.avatar
      }
    },
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
