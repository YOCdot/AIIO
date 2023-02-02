import { apiRequest } from "@/utils/request";

export function getLinks() {
    return apiRequest({
        url: "/links/",
        method: "get"
    })
}

export function getApp() {
    return apiRequest({
        url: "/app/",
        method: "get"
    })
}

export function postLogin(data) {
    return apiRequest({
        url: "/admin-login/",
        method: "post",
        data: data
    })
}