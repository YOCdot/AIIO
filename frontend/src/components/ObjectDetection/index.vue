<template>
  <div v-if="switchBtn === 0" class="hero min-h-screen bg-black">
    <div class="hero-content flex-col lg:flex-row fill-primary">
      <img :src=illusImg class="max-w-sm rounded-lg shadow-2xl" alt="yolo"/>
      <div class="text-white">
        <h1>
          <svg class="w-44 fill-current mb-6" viewBox="0 0 1120 534" version="1.1" xmlns="http://www.w3.org/2000/svg"
               xml:space="preserve"
               style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;"><g><g id="文字" transform="matrix(0.919561,0,0,1,-46.7656,0)"><text x="532.236px" y="435.298px" style="font-family:'SmileySans-Oblique', 'Smiley Sans';font-style:italic;font-size:450.886px;">AIIO</text></g><path
              id="底框"
              d="M1093.33,50.667c0,-13.246 -11.949,-24 -26.666,-24l-1013.33,-0c-14.717,-0 -26.666,10.754 -26.666,24l-0,432c-0,13.246 11.949,24 26.666,24l1013.33,-0c14.717,-0 26.666,-10.754 26.666,-24l0,-432Zm-26.666,20.286c-0,-11.196 -10.1,-20.286 -22.541,-20.286l-621.586,-0c-12.44,-0 -22.54,9.09 -22.54,20.286l-0,391.427c-0,11.197 10.1,20.287 22.54,20.287l621.586,-0c12.441,-0 22.541,-9.09 22.541,-20.287l-0,-391.427Zm-813.334,25.158l0,-22.778c0,-11.038 -8.961,-20 -20,-20l-160,0c-11.038,0 -20,8.962 -20,20l0,253.334c0,11.038 8.962,20 20,20l29.477,-0l0,113.333c0,11.038 8.962,20 20,20l160,-0c11.039,-0 20,-8.962 20,-20l0,-70.556l50.523,0c11.039,0 20,-8.961 20,-20l0,-253.333c0,-11.038 -8.961,-20 -20,-20l-100,-0Zm-80,250.556l-43.856,-0l0,92c0,8.094 6.572,14.666 14.667,14.666l117.333,0c8.095,0 14.667,-6.572 14.667,-14.666l-0,-49.223l-82.811,0c-11.038,0 -20,-8.961 -20,-20l0,-22.777Zm80,-133.334l0,113.334c0,11.038 -8.961,20 -20,20l-33.333,-0l0,1.444c0,8.095 6.572,14.667 14.667,14.667l61.477,-0l-0,-134.778c-0,-8.095 -6.572,-14.667 -14.667,-14.667l-8.144,0Zm0,-90.555l0,63.889l29.477,-0c11.039,-0 20,8.961 20,20l0,156.111l29.19,-0c8.095,-0 14.667,-6.572 14.667,-14.667l-0,-210.667c-0,-8.095 -6.572,-14.666 -14.667,-14.666l-78.667,-0Zm-150.523,197.222l0,-113.333c0,-11.039 8.962,-20 20,-20l50.523,-0l0,-70.556c0,-11.038 8.962,-20 20,-20l33.334,-0l-0,-1.444c-0,-8.095 -6.572,-14.667 -14.667,-14.667l-117.333,-0c-8.095,-0 -14.667,6.572 -14.667,14.667l0,210.666c0,8.095 6.572,14.667 14.667,14.667l8.143,-0Zm70.523,-106.667l-29.189,0c-8.095,0 -14.667,6.572 -14.667,14.667l0,92l43.856,-0l0,-106.667Zm53.334,0l-26.667,0l0,106.667l12,-0c8.095,-0 14.667,-6.572 14.667,-14.667l-0,-92Zm-0,-90.555l-12,-0c-8.095,-0 -14.667,6.571 -14.667,14.666l0,49.223l26.667,-0l-0,-63.889Z"/></g></svg>
        </h1>
        <h1 class="text-5xl font-bold fill-current">Object Detection, Online!</h1>
        <p class="py-6 text-current">Two original designed models are available.</p>
        <button class="btn bg-primary text-lg hover:mirror" @click="switchBtn += 1">DETECT ONLINE</button>
      </div>
    </div>
  </div>


  <div v-if="switchBtn === 1" class="hero min-h-screen max-h-full max-w-full bg-black">
    <div class="hero-content text-center">

      <div class="">
        <div class="text-5xl font-bold p-0 text-base-100">Two pre-trained models available:</div>

        <!--  选择模型  -->
        <ul v-if="model === 'fpdt'" class="my-16 flex items-center">
          <li @click="changeModel" :class="styleAct">
            <a>FPDT</a>
          </li>
          <li @click="changeModel" :class="styleDeact">
            <a>T-SSD</a>
          </li>
        </ul>
        <ul v-if="model === 'tssd'" class="my-16 flex items-center">
          <li @click="changeModel" :class="styleDeact">
            <a>FPDT</a>
          </li>
          <li @click="changeModel" :class="styleAct">
            <a>T-SSD</a>
          </li>
        </ul>


        <!--  文件上传  -->
        <input id="imgReceive" type="file" accept=".png,.jpeg,.jpg" @change="imgUpload($event)"
               class="file-input file-input-bordered file-input-primary w-full max-w-xs"/>
        <!--  图片加载  -->
        <label class="btn btn-primary ml-5" for="my-modal" @click="getImgDisplay">LOAD</label>
        <input type="checkbox" id="my-modal" class="modal-toggle"/>
        <div v-if="doneLoad === 1" class="modal">
          <div class="modal-box bg-neutral">
            <h3 class="text-4xl font-bold mt-10 text-secondary">
              Notice
            </h3>
            <div class="text-lg font-bold mt-3 mb-10 text-warning">
<!--              <p>Due to the asynchronism of JavaScript and how bad I've used it,</p>-->
<!--              <p>The image may not show up correctly.</p>-->
              <p>If the image didn't show up correctly, </p>
              <p class="inline-block">please hit that </p>
              <p class="text-base-100 rounded-md inline-block bg-primary mx-1 px-2">LOAD</p>
              <p class="inline-block"> button for several more times.</p>
              <p class="inline-block text-white mt-5">PS: I'll recommend you to  use image with its size smaller than (1000*1000).</p>
            </div>
            <div class="modal-action">
              <label for="my-modal" class="btn bg-success text-base-100" @click="getImgDisplay">OK</label>
            </div>
          </div>
        </div>


        <!--  提示信息  -->
<!--        <div class="my-10">-->
<!--          <div v-if="doneLoad !== 0" class="text-4xl font-bold text-info">-->
<!--            Image INFO:-->
<!--          </div>-->
<!--          <div v-if="doneLoad !== 0" class="text-lg font-bold mt-3 text-accent">-->
<!--            Image Size: {{ "(" + height + "*" + width + ")" }}-->
<!--          </div>-->
<!--        </div>-->

        <div class="mt-8">
          <div v-if="detStatus === 1" class="text-lg font-bold mt-3 text-warning">
            Detecting...
          </div>
          <div v-if="detStatus === 2" class="text-lg font-bold mt-3 text-error">
            Detected, {{ time_cost }}s spent.
          </div>
        </div>


        <!--  CANVAS  -->
        <canvas v-if="doneLoad !== 0" id="canvas" class="bg-neutral rounded-lg fill-current mt-8 max-w-screen-2xl max-h-screen" :width=width
                :height=height>
        </canvas>

        <button v-if="doneLoad !== 0" class="btn btn-primary text-3xl font-bold  mt-10" @click="postImage">DETECT!
        </button>


      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue";
import illusImg from "@/assets/images/detection.png";
// var imgSrc = ref("src/assets/images/example-dog.jpg");

let switchBtn = ref(0);
let model = ref("fpdt");
var doneLoad = ref(0);

var styleAct = "basis-1/2 p-3 mx-12 text-2xl text-white bg-primary hover:bg-primary hover:text-base-100 rounded-box"
var styleDeact = "basis-1/2 p-3 mx-12 text-2xl bg-neutral text-black hover:bg-primary hover:text-base-100 rounded-box"


function changeModel() {
  // console.log(model.value);
  if (model.value === "fpdt") {
    model.value = "tssd";
  } else if (model.value === "tssd") {
    model.value = "fpdt";
  } else {
    console.log("Error Model Choice!");
  }
}

// 图片
var imgSrc = ref(undefined);
var height = ref(undefined);
var width = ref(undefined);

// 上传
function imgUpload(event) {
  //e.target指向事件执行时鼠标所点击区域的那个元素，那么为input的标签，
  // 可以输出 e.target.files 看看，这个files对象保存着选中的所有的图片的信息。
  // console.log(event.target.files);
  let file = event.target.files[0];
  // console.log(file.type);


  //  创建一个FileReader()对象，它里面有个readAsDataURL方法
  var reader = new FileReader();
  // readAsDataURL方法可以将上传的图片格式转为base64,然后在存入到图片路径,
  //这样就可以上传电脑任意位置的图片
  reader.readAsDataURL(file);

  /*当读取操作成功完成时调用*/
  reader.onload = function () {
    // console.log(reader.readyState);

    // console.log(e); //查看对象
    // console.log(this.result);//要的数据 这里的this指向FileReader（）对象的实例reader

    imgSrc.value = this.result;

  }


}

function getImgDisplay() {

  let img = new Image();
  img.src = imgSrc.value;
  height.value = img.height;
  width.value = img.width;
  doneLoad.value += 1;

  // console.log(height.value, width.value);

  let ctx = document.getElementById('canvas').getContext('2d');

  // img.src = "src/assets/images/example-dog.jpg";

  img.onload = function () {
    ctx.drawImage(img, 0, 0);
  }

}

function drawRects(data) {

  console.log(data.pred);
  let predictions = data.pred;

  // 获取画笔 & 上下文对象
  let ctx = document.getElementById('canvas').getContext('2d');

  for (let idx in predictions) { // 绘制图形
    // console.log(idx, predictions[idx]);

    ctx.fillStyle="red";
    ctx.font = "18px SmileySans"
    ctx.fillStyle="#FF0000";
    ctx.fillText(idx,predictions[idx][0], predictions[idx][1] - 4);

    //  - 绘制矩形: fillRect(位置x, 位置y, 宽度, 高度)
    ctx.strokeStyle = "#FF0000";
    ctx.lineWidth = 3;
    ctx.strokeRect(predictions[idx][0], predictions[idx][1], predictions[idx][2], predictions[idx][3]);
  }
}


import {postDetection} from "@/api";

var detStatus = ref(0);
var time_cost = ref(0);
var pred_obj = ref(null);

function postImage() {
  detStatus.value = 1;
  postDetection({
    model: model.value,
    img: imgSrc.value,
  }).then(result => {
    console.log(result.data);
    time_cost.value = result.data.time
    pred_obj.value = result.data.pred;
    drawRects(result.data);
    detStatus.value = 2;
  }).catch((error) => {
    console.log(error);
  });
}


</script>
