import axios from "axios";

let getLinks = (urlParam) => {
  axios
    .get(urlParam)
    .then((result) => {
      console.log(result.data); // 响应对象
      return result.data;
    })
    .catch((err) => {
      console.log(err);
      return err;
    });
};

export { getLinks };
