import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../views/Dashboard.vue';
import ServerList from '../components/ServerList.vue';

const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/servers', name: 'ServerList', component: ServerList },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
