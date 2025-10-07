import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/home.vue'
import Upload from '../pages/upload.vue'
import Chat from '../pages/chat.vue'
import Login from '../pages/login.vue'
import Register from '../pages/register.vue'
import Dashboard from '../pages/dashboard.vue'
import Admin from '../pages/admin.vue'
import { isLoggedIn, loadUser } from '../utils/auth'

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/upload', name: 'upload', component: Upload, meta: { requiresAuth: true } },
  { path: '/chat', name: 'chat', component: Chat, meta: { requiresAuth: true } },
  { path: '/dashboard', name: 'dashboard', component: Dashboard, meta: { requiresAuth: true } },
  {
    path: '/admin',
    name: 'admin',
    component: Admin,
    meta: { requiresAuth: true, requiresAdmin: true },
  },
  { path: '/login', name: 'login', component: Login },
  { path: '/register', name: 'register', component: Register },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (!to.meta.requiresAuth) {
    next()
    return
  }

  if (!isLoggedIn()) {
    next({ name: 'login', query: { redirect: to.fullPath } })
    return
  }

  const user = loadUser()
  if (to.meta.requiresAdmin && !user?.is_admin) {
    next({ name: 'dashboard' })
    return
  }

  next()
})

export default router
