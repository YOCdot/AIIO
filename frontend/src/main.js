import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";

import axios from "axios";
import VueAxios from "vue-axios";

import "@/assets/common.css";

const app = createApp(App);

app.use(router); // 绑定路由
app.use(VueAxios, axios); // 使用 axios

app.mount("#app");
