import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './components/MyForm.vue'
import AboutView from './components/HelloWorld.vue'

const routes = [
    { path: '/', component: HomeView },
    { path: '/blog', component: AboutView },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router