<template>
  <div class="hero min-h-screen bg-black">
    <div class="hero-content flex-col lg:flex-row">
      <img :src=illusImg class="max-w-sm rounded-lg shadow-2xl"/>
      <div>
        <h1>
          <img :src="detLogo" alt="logo" class="h-32 w-38 mb-3"/>
        </h1>
        <h1 class="text-5xl font-bold text-blue-100">Object Detection, Online!</h1>
        <p class="py-6 text-blue-300">Two original designed models are available.</p>
        <a href="#detectBed">
          <button class="btn bg-blue-900 w-32" @click="goDetect">DETECT ONLINE</button>
        </a>
      </div>
    </div>
  </div>




  <div id="detectBed" class="hero min-h-screen bg-base-200">
    <div class="hero-content text-center">

        <div class="tabs tabs-boxed">
          <a class="tab">Tab 1</a>
          <a class="tab tab-active">Tab 2</a>
          <a class="tab">Tab 3</a>
        </div>

      <div class="max-w-md">
        <h1 class="text-5xl font-bold">Hello there</h1>
        <p class="py-6">Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.</p>
        <button class="btn btn-primary">Get Started</button>
      </div>
    </div>
  </div>

</template>

<script setup>
import illusImg from "@/assets/images/detection.png";
import detLogo from "/src/assets/icons/logo-white.svg"


// import imgSrc from "@/assets/images/example-dog.jpg";
// let imgDisplay = document.getElementById("imgDisplay");
//
// // 1. 找到画布
// let c1 = document.getElementById("cBed");
// // 2. 获取画笔 & 上下文对象
// let ctx = c1.getContext("2d");
// // 3. 绘制图形
// // 3.1 绘制矩形: fillRect(位置x, 位置y, 宽度, 高度)
// ctx.drawImage(imgDisplay, 0, 0);
// ctx.strokeStyle="#FF0000";
// ctx.strokeRect(100, 200, 300, 300);


function goDetect() {
  let dest = document.getElementById("#canvasEmbed");
  window.scrollTo({
    top: dest,
    behavior: 'smooth'
  })
}

</script>
