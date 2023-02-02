<script setup>
import logo from "@/assets/black-logo-hires.png";
import github_icon from "@/assets/github.svg";

import {RouterLink, RouterView} from "vue-router";

import {ref} from "vue";
import {getApp} from "@/api";

let appItems = ref([]);
getApp().then(result => {
  appItems.value = result.data;
});
</script>

<template>
  <!--  导航条: 开始  -->
  <header class="p-3 header-custom" style="margin-bottom: 200px">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">

        <router-link class="d-flex align-items-center mb-2 mb-lg-0 text-black text-decoration-none" height="32" role="img" to="/">
          <img :src=logo alt="AIIO" height="60">
        </router-link>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0" style="font-size: 30px">
          <li>
            <router-link class="nav-link px-2 text-secondary text-black" to="object-detection" style="margin: 0 20px">
              目标检测
            </router-link>
          </li>
          <li>
            <router-link class="nav-link px-2 text-secondary text-black" to="personal-links">
              个人链接
            </router-link>
          </li>
        </ul>

<!--        <div class="text-end"></div>-->
      </div>
    </div>
  </header>

  <!--  导航条: 结束  -->

  <!--  路由页面: 开始  -->
  <router-view></router-view>
  <!-- 路由页面: 结束 -->

  <!--  页脚: 开始  -->
  <footer class="card-foot footer navbar-custom" style="margin-top: 200px">

    <div class="container text-center">

      <div class="self-introduce">

        <div>我是 yoc 🫡 ！</div>
        <div >这是我的个人主页，同时也是我的Playground！</div>
        <div>
          是一名在读的人工智能研究生，研究方向是：目标检测算法，业余兴趣是学习各种计算机技术。
        </div>
        <div>
          © This project is powered by
          <a>
            <img class="tech-img" alt="vue" src="/src/assets/vue.png"/>
          </a>
          &
          <a>
            <img class="tech-img" alt="dj" src="https://www.djangoproject.com/m/img/logos/django-logo-negative.svg"/>
          </a>
          , implemented by yoc.
        </div>

      </div>

      <hr>

      <div class="container text-center">
        <div class="row">
          <div class="col align-self-start">
            <router-link class="footer-item" to="admin-login">
              功能测试
            </router-link>
          </div>
          <div class="col align-self-center">
            <a class="footer-item" href="https://beian.miit.gov.cn/" target="_blank">
              沪ICP备2022008973号-1
            </a>
          </div>
          <div class="col align-self-end">
            <a class="footer-item" href="https://github.com/YOCdot" target="_blank">
              <img
                  :src="github_icon"
                  alt="logo"
                  style="height: 18px"
              />
            </a>
          </div>
        </div>
      </div>

    </div>
  </footer>
  <!--  页脚: 结束  -->

</template>

<style scoped>


.header-custom {
  /*height: 80px;*/
  background-color: #fffa;
  backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  -webkit-backdrop-filter: blur(10px) saturate(160%) contrast(180%);
}

.navbar-item {
  font-size: 28px;
  margin-left: 20px;
}


.self-introduce {
  font-size: 15px;
  /*color: gray;*/
  /*padding-bottom: 130px;*/
}

.tech-img {
  height: 18px;
}

.footer {
  height: 185px;
  float: bottom;
  padding: 20px 0 20px 0;
  background-color: #fffa;
  backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  -webkit-backdrop-filter: blur(10px) saturate(160%) contrast(180%);
}

.copy-right {
  margin-top: 50px;
}

.footer-item {
  font-size: 15px;
  /*display: inline-block;*/
  text-align: center;
  color: black;
  text-decoration: none;
}
</style>
