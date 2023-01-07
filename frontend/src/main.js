import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";

import "@/assets/common.css";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// import {axios} from "axios"

const app = createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}  // ele-icon

app.use(router); // 绑定路由
app.use(ElementPlus); // 使用 ele
// app.use(axios); // 使用 axios

app.mount("#app");
