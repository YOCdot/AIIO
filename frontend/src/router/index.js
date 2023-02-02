import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/components/MainHome.vue"),
  },
  {
    path: "/personal-links",
    component: () => import("@/components/PersonalLinks.vue"),
  },
  {
    path: "/object-detection",
    // name: "object-detections",
    component: () => import("@/components/ObjectDetection.vue"),
  },
  {
    path: "/admin-login",
    component: () => import("@/components/AdminLogin.vue"),
  },
  {
    path: "/com-test",
    component: () => import("@/components/ComTest.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
