import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";

import axios from "axios";
import VueAxios from "vue-axios";

import "@/style.css";

const app = createApp(App);

app.use(router); // 绑定路由
app.use(VueAxios, axios); // 使用 axios

app.mount("#app");
