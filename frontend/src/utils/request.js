import axios from "axios";

export function apiRequest(config) {

    // axios 实例
    let instance = axios.create({
        baseURL: "http://localhost:8000/api",
        timeout: 5000,
    });

    // 发送真正的请求
    return instance(config);
}
