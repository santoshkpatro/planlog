import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/pages/Login.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/pages/Register.vue'),
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/pages/Profile.vue'),
      meta: { requiresAuth: true }
    },
  ],
})

router.beforeEach((to, from) => {
  const userData = localStorage.getItem('user')

  if(to.meta.requiresAuth) {
    if(!userData) {
      return {
        path: '/login',
        query: {
          redirect: to.fullPath
        }
      }
    }
  }
})

export default router
