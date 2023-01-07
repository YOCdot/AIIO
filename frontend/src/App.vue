<script setup>
import logo from "@/assets/white-logo-midres.png";

import { RouterLink, RouterView } from "vue-router";

import { h } from "vue";
import { ElDivider } from "element-plus";

const spacer = h(ElDivider, { direction: "vertical" });
</script>

<template>
  <el-container class="container">
    <el-header class="header">
      <el-row :gutter="24" class="header-row">
        <el-col :span="8" class="header-col">
          <router-link class="header-text" to="personal-links"
            >个人链接</router-link
          >
        </el-col>
        <el-col :span="8" class="header-col">
          <router-link class="nav-links-img" to="/" style="width: 100px">
            <div
              class="logo-container"
              style="
                width: 100px;
                vertical-align: center;
                text-align: center;
                display: inline-block;
                margin: 0;
              "
            >
              <el-image
                :src="logo"
                alt="logo"
                :fit="'fill'"
                style="display: inline-block"
              ></el-image>
            </div>
          </router-link>
        </el-col>
        <el-col :span="8" class="header-col">
          <router-link class="header-text" to="object-detection"
            >目标检测</router-link
          >
        </el-col>
      </el-row>
    </el-header>
    <el-main style="padding: 0; margin: 0">
      <router-view></router-view>
    </el-main>
    <el-footer style="padding: 0; margin: 0">
      <el-space :size="1" :spacer="spacer" style="height: 100%">
        <router-link
          class="footer-item"
          to="com-test"
          style="vertical-align: middle"
          >API测试</router-link
        >
        <a class="footer-item" href="https://beian.miit.gov.cn/" target="_blank"
          >沪ICP备2022008973号-1</a
        >
      </el-space>
    </el-footer>
  </el-container>
</template>

<style scoped>
.container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.header {
  padding: 0;
  height: 60px;
  text-align: center;
  background-color: rgb(49, 49, 50);
}

.header-row {
  height: 100%;
}

.header-col {
  height: 100%;
  vertical-align: center;
}

.header-text {
  vertical-align: center;
  text-align: center;
  display: inline-block;
  margin: 0;
  padding: 0;
  text-decoration: none;
  font-size: 28px;
  color: rgba(214, 214, 214);
}

.el-footer {
  height: 50px;
  text-align: center;
  vertical-align: center;
  background-color: rgb(49, 49, 50);
}
.footer-item {
  font-size: 15px;
  display: inline-block;
  text-align: center;
  color: rgb(214, 214, 214);
  text-decoration: none;
}

/*.footer-item {*/
/*  color: grey;*/
/*  text-decoration: none;*/
/*  height: 100%;*/
/*}*/

.footer-item:hover,
.nav-links-text:hover,
.nav-links-img {
  color: white;
  text-decoration: none;
  text-align: center;
}

.nav-links-img {
  display: inline-block;
  margin: 5px;
  text-align: center;
  text-decoration: none;
}
</style>
