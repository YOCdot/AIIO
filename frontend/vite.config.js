import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  // 代理配置
  server: {
    proxy: {
      "/apis": {
        target: "http://127.0.0.1:8000/apis", //目标url
        changeOrigin: true, //支持跨域
        rewrite: (path) => path.replace(/^\/apis/, ""),
        //重写路径,替换/api
      },
    },
    host: "0.0.0.0",
  },
});
