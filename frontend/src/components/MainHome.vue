<script setup>
// import bgImg from "@/assets/images/bg-image.jpg";
</script>

<template>
  <div class="hero min-h-screen fill-current bg-[url('@/assets/images/bg-image.jpg')]">
    <!--    <div class="hero-overlay">-->
    <!--    </div>-->
    <div class="hero-content text-center text-neutral-content ">
      <div class="max-w-full">
        <h1 class="mb-5 text-5xl font-bold text-white">Welcome to @yoc 's personal website!</h1>
        <h2 class="my-16 text-3xl font-bold text-white">Funny tools provided, please have fun:</h2>

        <ul class="space-x-5">
          <li class="backdrop-blur-md min-w-full px-5 py-8 text-primary rounded-lg hover:text-base-100 hover:bg-primary">
            <router-link to="object-detection">
              <svg class="h-28 mx-auto fill-current" viewBox="0 0 1120 534" version="1.1" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" style="font-family: SmileySans;fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;"><g><g id="文字" transform="matrix(0.919561,0,0,1,-46.7656,0)"><text x="532.236px" y="435.298px" style="font-family:SmileySans;font-size:450.886px;">AIIO</text></g><path id="底框" d="M1093.33,50.667c0,-13.246 -11.949,-24 -26.666,-24l-1013.33,-0c-14.717,-0 -26.666,10.754 -26.666,24l-0,432c-0,13.246 11.949,24 26.666,24l1013.33,-0c14.717,-0 26.666,-10.754 26.666,-24l0,-432Zm-26.666,20.286c-0,-11.196 -10.1,-20.286 -22.541,-20.286l-621.586,-0c-12.44,-0 -22.54,9.09 -22.54,20.286l-0,391.427c-0,11.197 10.1,20.287 22.54,20.287l621.586,-0c12.441,-0 22.541,-9.09 22.541,-20.287l-0,-391.427Zm-813.334,25.158l0,-22.778c0,-11.038 -8.961,-20 -20,-20l-160,0c-11.038,0 -20,8.962 -20,20l0,253.334c0,11.038 8.962,20 20,20l29.477,-0l0,113.333c0,11.038 8.962,20 20,20l160,-0c11.039,-0 20,-8.962 20,-20l0,-70.556l50.523,0c11.039,0 20,-8.961 20,-20l0,-253.333c0,-11.038 -8.961,-20 -20,-20l-100,-0Zm-80,250.556l-43.856,-0l0,92c0,8.094 6.572,14.666 14.667,14.666l117.333,0c8.095,0 14.667,-6.572 14.667,-14.666l-0,-49.223l-82.811,0c-11.038,0 -20,-8.961 -20,-20l0,-22.777Zm80,-133.334l0,113.334c0,11.038 -8.961,20 -20,20l-33.333,-0l0,1.444c0,8.095 6.572,14.667 14.667,14.667l61.477,-0l-0,-134.778c-0,-8.095 -6.572,-14.667 -14.667,-14.667l-8.144,0Zm0,-90.555l0,63.889l29.477,-0c11.039,-0 20,8.961 20,20l0,156.111l29.19,-0c8.095,-0 14.667,-6.572 14.667,-14.667l-0,-210.667c-0,-8.095 -6.572,-14.666 -14.667,-14.666l-78.667,-0Zm-150.523,197.222l0,-113.333c0,-11.039 8.962,-20 20,-20l50.523,-0l0,-70.556c0,-11.038 8.962,-20 20,-20l33.334,-0l-0,-1.444c-0,-8.095 -6.572,-14.667 -14.667,-14.667l-117.333,-0c-8.095,-0 -14.667,6.572 -14.667,14.667l0,210.666c0,8.095 6.572,14.667 14.667,14.667l8.143,-0Zm70.523,-106.667l-29.189,0c-8.095,0 -14.667,6.572 -14.667,14.667l0,92l43.856,-0l0,-106.667Zm53.334,0l-26.667,0l0,106.667l12,-0c8.095,-0 14.667,-6.572 14.667,-14.667l-0,-92Zm-0,-90.555l-12,-0c-8.095,-0 -14.667,6.571 -14.667,14.666l0,49.223l26.667,-0l-0,-63.889Z"/></g></svg>
              <p class="text-5xl">Object Detection</p>
            </router-link>
          </li>

<!--          <li class="rounded-lg bg-secondary w-36 mx-auto">-->
<!--            <a>Others coming soon...</a>-->
<!--          </li>-->
        </ul>

      </div>
    </div>
  </div>
</template>