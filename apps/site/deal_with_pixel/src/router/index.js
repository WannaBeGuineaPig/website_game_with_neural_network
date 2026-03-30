import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/MenuView.vue'),
    },
    {
      path: '/authorization',
      name: 'authorization',
      component: () => import('../views/AuthorizationView.vue'),
    },
    {
      path: '/personal-account',
      name: 'personalAccount',
      component: () => import('../views/PersonalAccountView.vue'),
    },
  ],
})

export default router
