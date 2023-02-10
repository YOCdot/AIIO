<template>
  <h1 class="banner">🌏 个人链接</h1>

  <ul class="link-table">
    <li class="link-item" v-for="linkItem in linkItems" >
      <a class="link-element" :href=linkItem.link style="text-decoration: none" >
        <img :src=linkItem.icon :alt=linkItem.title width="20"/>
        {{ linkItem.title }}
      </a>
    </li>

  </ul>
</template>

<script setup>
// import "@/styles/PersonalLinks.css";

import {ref} from "vue";
import {getLinks} from "@/api";

let linkItems = ref([]);

getLinks().then(result => {
  linkItems.value = result.data;
});

</script>
