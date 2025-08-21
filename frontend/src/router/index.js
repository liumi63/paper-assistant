import { createRouter, createWebHistory } from 'vue-router'
import home from '../pages/home.vue'
// import Upload from '../pages/Upload.vue'
// import Chat from '../pages/Chat.vue'

const routes = [
  { path: '/home', component: home },
//   { path: '/upload', component: Upload },
//   { path: '/chat', component: Chat }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
