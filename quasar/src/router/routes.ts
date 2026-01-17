import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/IndexPage.vue') }],
  },
  {
    path: '/blog',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/BlogPage.vue') }],
  },
  {
    path: '/login',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/LoginPage.vue') }],
  },
  {
    path: '/signup',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/SignupPage.vue') }],
  },
  {
    path: '/cabinet',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/CabinetPage.vue') }],
  },
  {
    path: '/post-edit',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/PostEdit.vue') }],
  },
  {
    path: '/post-edit/:id(.*)',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/PostEdit.vue') }],
  },
  {
    path: '/post-view/:id(.*)',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/PostView.vue') }],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
