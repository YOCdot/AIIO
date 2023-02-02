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
import {ref} from "vue";
import {getLinks} from "@/api";

let linkItems = ref([]);

getLinks().then(result => {
  linkItems.value = result.data;
});

</script>

<style scoped>

.link-table {
  box-sizing: border-box;
  list-style: none;
  margin: auto auto 200px auto;
  /*padding: 2em;*/
  padding: 0;
  max-width: 300px;
}

.link-item {
  background-color: #fffa;
  backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  -webkit-backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  border-radius: 10em;
  margin: 1.4em 0;
  box-shadow: rgb(28 32 93 / 24%) 0px 2px 8px 0px;
}

.link-item:hover {
  background-color: #2e2e2e;
  backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  -webkit-backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  border-radius: 10em;
  margin: 1.4em 0;
  box-shadow: rgb(49 49 50 / 24%) 0px 2px 8px 0px;
}

.link-element {
  color: black;
  text-decoration: none;
  text-align: center;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 0.5em;
  padding: 1em;
}

.link-element:hover {
  color: white;
}
</style>
