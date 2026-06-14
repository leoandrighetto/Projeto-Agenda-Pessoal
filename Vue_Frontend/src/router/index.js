import { createWebHistory, createRouter } from "vue-router";

import HomeView from "../pages/HomeView.vue";
import RegisterView from "../pages/authentication/RegisterView.vue";

const routes = [
  { path: "/", component: HomeView },
  { path: "/register", component: RegisterView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
