<template>
  <h1 class="banner">API测试</h1>
  <div class="mid-con">
    <div>
      <h2>响应式数据：{{ vals }}</h2>
      <el-button @click="valPlus"> +1</el-button>
    </div>

    <div>
      <h2 class="banner">AXIOS请求测试</h2>
      <h2>GET 请求 - 参数默认空</h2>
      <el-input
        type="text"
        v-model="bookGetParam"
        placeholder="参数"
        style="width: 80px; margin-right: 10px"
      />
      <el-button @click="getAction(bookGetParam)"> GET </el-button>
      <div>
        <h3>数据展示</h3>
        <ul>
          <li v-for="book in books" style="list-style-type: none">
            <el-space :size="10" spacer="|">
              <span>ID：{{ book.id }}</span>
              <span>书名：{{ book.btitle }}</span>
              <span>发布日期：{{ book.bpub_date }}</span>
              <span>阅读量：{{ book.bread }} </span>
              <span>评论量：{{ book.bcomment }}</span>
            </el-space>
          </li>
        </ul>
      </div>

      <br />

      <hr />

      <h2>POST 请求 - 添加书籍</h2>
      <el-input
        type="text"
        v-model="bookTitle"
        placeholder="书名"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="bookPubDate"
        placeholder="发布时间"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="bookRead"
        placeholder="阅读量"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="bookComment"
        placeholder="评论量"
        style="width: 80px; margin-right: 10px"
      />
      <div v-if="addFlag !== null">
        <h3>添加成功：{{ resultTitle }}</h3>
      </div>
      <el-button @click="postAction"> POST </el-button>

      <br />

      <h2>DELETE 请求</h2>
      <el-input
        type="text"
        v-model="deleteId"
        placeholder="删除的id"
        style="width: 80px; margin-right: 10px"
      />
      <div v-if="delFlag">
        <h3>删除成功！</h3>
      </div>
      <el-button @click="deleteAction(deleteId)"> DELETE </el-button>

      <br />

      <h2>PUT 请求 - 修改书籍</h2>
      <el-input
        type="text"
        v-model="putId"
        placeholder="ID"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="putTitle"
        placeholder="书名"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="putPubDate"
        placeholder="发布时间"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="putRead"
        placeholder="阅读量"
        style="width: 80px; margin-right: 10px"
      />
      <el-input
        type="text"
        v-model="putComment"
        placeholder="评论量"
        style="width: 80px; margin-right: 10px"
      />
      <el-button @click="putAction(putId)"> PUT</el-button>
      <div v-if="putFlag">
        <h3>修改成功：{{ resultTitle }}</h3>
        <el-space :size="10" spacer="|">
          <span>ID：{{ putId }}</span>
          <span>书名：{{ pTitle }}</span>
          <span>发布日期：{{ pPubDate }}</span>
          <span>阅读量：{{ pRead }} </span>
          <span>评论量：{{ pComment }}</span>
        </el-space>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

let vals = ref(0);

function valPlus() {
  vals.value += 1;
}

// get
let books = ref(""); // 初始化值
let bookGetParam = ref(null);

// post
let bookTitle = ref(null);
let bookPubDate = ref(null);
let bookRead = ref(null);
let bookComment = ref(null);
let addFlag = ref(null);
let resultTitle = ref(null);

// delete
let deleteId = ref(null);
let delFlag = ref(false);

// put
let putFlag = ref(false);
let putId = ref(null);
let putTitle = ref(null);
let putPubDate = ref(null);
let putRead = ref(null);
let putComment = ref(null);
let pTitle = ref(null);
let pPubDate = ref(null);
let pRead = ref(null);
let pComment = ref(null);

// patch

const getAction = (getParam) => {
  console.log(getParam);
  if (getParam === null) {
    // 不带参数的 get
    axios
      .get("/apis/books")
      .then((result) => {
        // console.log(result); // 响应对象
        books.value = result.data;
        console.log(books);
      })
      .catch((err) => {
        console.log(err);
      });
  } else {
    // 带参数的 get
    axios
      .get("/apis/books/" + getParam)
      .then((result) => {
        // console.log(result); // 响应对象
        books.value = [result.data];
        console.log(books);
        bookGetParam.value = null;
      })
      .catch((err) => {
        console.log(err);
      });

    // 带有多个参数的 get
    // axios
    //   .get("#", {
    //     params: {
    //       age: 18,
    //       gender: 1,
    //     },
    //   })
    //   .then((result) => {
    //     // console.log(result); // 响应对象
    //     books.value = [result.data];
    //     console.log(books);
    //     bookGetParam.value = null;
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   });
  }
};
const postAction = () => {
  axios
    .post("/apis/books", {
      btitle: bookTitle.value,
      bpub_date: bookPubDate.value,
      bread: bookRead.value,
      bcomment: bookComment.value,
    })
    .then((result) => {
      console.log(result.data);
      addFlag.value = true;
      resultTitle.value = result.data.btitle;
    })
    .catch((err) => {
      console.log(err);
    });
};
const deleteAction = (delId) => {
  // console.log("/apis/books/" + delId);
  if (delId !== null) {
    axios
      .delete("/apis/books/" + delId)
      .then((result) => {
        delFlag.value = true;
        console.log(result.data);
        deleteId.value = null;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};

const putAction = (putPk) => {
  if (putPk !== null) {
    console.log("/apis/books/" + putPk);
    axios
      .put("/apis/books/" + putPk + "/", {
        id: putPk.value,
        btitle: putTitle.value,
        bpub_date: putPubDate.value,
        bread: putRead.value,
        bcomment: putComment.value,
      })
      .then((result) => {
        console.log(result.data);
        putFlag.value = true;
        pTitle.value = result.data.title;
        pPubDate.value = result.data.bpub_date;
        pRead.value = result.data.bread;
        pComment.value = result.data.bcomment;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};

const patchAction = () => {};
</script>

<style scoped>
html,
body,
h1,
h2,
h3 {
  color: white;
  align-items: center;
  text-align: center;
}

.mid-con {
  text-align: center;
  align-items: center;

  margin-bottom: 200px;
}

#components-layout-demo-fixed .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}

.site-layout .site-layout-background {
  background: #fff;
}

[data-theme="dark"] .site-layout .site-layout-background {
  background: #141414;
}
</style>
