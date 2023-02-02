<template>

  <div class=" container text-center">

      <form id="formSubmit">
        <h1 class="banner">Only Available for Myself</h1>

        <div class="form-floating w-25" style="margin: 20px auto">
          <input type="text" class="form-control" id="nameInput" placeholder="Name" v-model="name">
          <label for="nameInput">Name</label>
        </div>
        <div class="form-floating w-25" style="margin: 20px auto">
          <input type="password" class="form-control" id="passwordInput" placeholder="Password" v-model="password">
          <label for="passwordInput">Password</label>
        </div>

<!--        <div>-->
<!--          <input type="text" v-model="hashPwd" />-->
<!--        </div>-->

        <button class="w-25 btn btn-lg btn-primary" type="submit" @click="postItems" style="margin: 80px 0 150px 0; width: 50px">
          👌🏻
          <input v-model="hashedPassword" type="text"/>
        </button>

      </form>

  </div>

</template>

<script setup>

import {ref} from "vue";
import {postLogin} from "@/api";
// import PersonalLinks from "@/components/PersonalLinks.vue";
// import {jwt_generate} from "@/authentication/jwt";
import sha256 from "crypto-js/sha256"


let name = ref(null);
let password = ref(null);

let hashedPassword = sha256(password.value);

function postItems() {
  postLogin({
    "name": name.value,
    "password": password.value,
  }).then(result => {
    console.log(result.data);
  });
}

</script>

<style scoped>
.login-bg {
  background-color: #fffa;
  backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  -webkit-backdrop-filter: blur(10px) saturate(160%) contrast(180%);
}
</style>