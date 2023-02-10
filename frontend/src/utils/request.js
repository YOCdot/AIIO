import axios from "axios";

export function apiRequest(config) {

    // axios 实例
    let instance = axios.create({
        baseURL: "/api",
        timeout: 300000, // 5min
    });

    // 发送真正的请求
    return instance(config);
}
