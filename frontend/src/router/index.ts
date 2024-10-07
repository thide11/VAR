import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import MeetView from '@/views/MeetView.vue'
import HomeViewVue from '@/views/HomeView.vue';

console.log(import.meta?.env?.BASE_URL);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeViewVue
    },
    {
      path: '/meets/:meetId',
      // name: 'meets',
      component: MeetView
    },
  ]
})

export default router
