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
    // 跨域解决
    // proxy: {
    //   "/api": {
    //     target: "http://127.0.0.1:8000/api", // api目标url
    //     changeOrigin: true, //支持跨域
    //     rewrite: (path) => path.replace(/^\/api/, ""),
    //     // 重写路径, 替换/api
    //   },
    //   "/media": {
    //     target: "http://127.0.0.1:8000/media", // media目标url
    //     changeOrigin: true, //支持跨域
    //     rewrite: (path) => path.replace(/^\/media/, ""),
    //     // 重写路径, 替换 `/media`
    //   },
    // },
    host: "0.0.0.0",
  },
});
