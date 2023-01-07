<template>
  <h1 class="banner">🌏 个人链接</h1>

  <ul class="link-table">
    <li class="link-item">
      <a
        class="link-element"
        href="https://twitter.com/yoc717"
        style="text-decoration: none"
      >
        <img src="@/assets/twitter.svg" alt="Twitter" width="20" />
        Twitter
      </a>
    </li>

    <li class="link-item">
      <a
        class="link-element"
        href="https://www.instagram.com/yoc717/"
        style="text-decoration: none"
      >
        <img src="@/assets/instagram.svg" alt="Instagram" width="20" />
        Instagram
      </a>
    </li>

    <li class="link-item">
      <a
        class="link-element"
        href="https://www.facebook.com/profile.php?id=100079059970137"
        style="text-decoration: none"
      >
        <img src="@/assets/facebook.svg" alt="Facebook" width="20" />
        Facebook
      </a>
    </li>

    <li class="link-item">
      <a
        class="link-element"
        href="https://weibo.com/u/2707953287"
        style="text-decoration: none"
      >
        <img src="@/assets/weibo.svg" alt="Weibo" width="20" />
        Weibo
      </a>
    </li>

    <li class="link-item">
      <a
        class="link-element"
        href="https://space.bilibili.com/2703022"
        style="text-decoration: none"
      >
        <img src="@/assets/bilibili.svg" alt="Bilibili" width="20" />
        Bilibili
      </a>
    </li>
  </ul>
</template>

<script setup>
import { getLinks } from "@/utils/linksRequests";

let linkObj = getLinks("/apis/books/");
console.log(linkObj);
</script>

<style scoped>
header {
  margin-top: 3em;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

header > img {
  width: 6em;
  height: 6em;
  border-radius: 100%;
  border: 1px solid #fff;
  box-shadow: rgb(28 32 93 / 24%) 0px 2px 8px 0px;
}

header > h1 {
  display: inline-block;
  font-size: 0.8em;
  font-weight: bold;
  border-radius: 1em;
  background-color: #000a;
  color: #fff;
  padding: 0.3em 0.6em;
  border: 1px solid #fffa;
  backdrop-filter: blur(10px) saturate(160%) contrast(180%);
  -webkit-backdrop-filter: blur(10px) saturate(160%) contrast(180%);
}

.link-table {
  box-sizing: border-box;
  list-style: none;
  margin: 0 auto;
  padding: 2em;
  max-width: 250px;
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

.breadcrumb {
  background: none;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 0.5em;
  padding: 1em;
}
</style>
