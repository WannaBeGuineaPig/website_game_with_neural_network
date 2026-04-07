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
      path: '/registration',
      name: 'registration',
      component: () => import('../views/RegistrationView.vue'),
    },
    {
      path: '/personal-account',
      name: 'personalAccount',
      component: () => import('../views/PersonalAccountView.vue'),
    },
    {
      path: '/game-lobby',
      name: 'gameLobby',
      component: () => import('../views/LobbyGameView.vue'),
    },
    {
      path: '/game',
      name: 'game',
      props: true,
      component: () => import('../views/GameView.vue'),
    },
  ],
})

export default router
