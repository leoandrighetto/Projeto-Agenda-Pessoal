import { createWebHistory, createRouter } from "vue-router";

import HomeView from "../pages/HomeView.vue";

if(HomeView){
    console.log("HomeView Passou")
}

const routes = [
    { path: "/", component: HomeView }
];

const router = createRouter({
    history: createWebHistory(),
    routes});

export default router;
