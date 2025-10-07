import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/home.vue'
import Upload from '../pages/upload.vue'
import Chat from '../pages/chat.vue'
import Login from '../pages/login.vue'
import Register from '../pages/register.vue'

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/upload', name: 'upload', component: Upload },
  { path: '/chat', name: 'chat', component: Chat },
  { path: '/login', name: 'login', component: Login },
  { path: '/register', name: 'register', component: Register },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
