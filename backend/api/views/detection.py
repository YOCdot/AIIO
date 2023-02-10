# ---*--- File Information ---*---
# @File       :  detection.py
# @Date&Time  :  2023-02-01, 16:29:26
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


import io
import time
import os
import base64
import cv2
from PIL import Image
import numpy as np

from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet  # 视图集 - ViewSet
from rest_framework.decorators import action  # 动作装饰器 (装饰类内方法令路由进行注册)


from api.models import Links, Admin
from api.serializers.model_serializers import LinksModelSerializer, AdminModelSerializer

from api.detection import ONNXModel


class ObjectDetection(APIView):
    """ 目标检测 """

    def post(self, request):
        print(settings.MEDIA_ROOT)

        # print(request.data)
        model_choice = request.data["model"]
        raw_base64 = request.data["img"]
        raw_base64 = raw_base64.split(",")
        meta_data = raw_base64[0]  # data:image/jpeg;base64
        img_data = "".join(raw_base64[1:])

        img = base64.b64decode(img_data)

        # 保存
        img_type = meta_data.split("/")[1].split(";")[0]
        ctime = time.strftime('%Y%m%d-%H%M%S', time.localtime())
        # print(img_type)

        store_file = settings.MEDIA_ROOT + "/detections/" + ctime + "." + img_type

        # 以保存的方式进行判断
        file = open(store_file, 'wb')
        file.write(img)
        file.close()

        # 以读入内存的方式进行判断
        # img = io.BytesIO(img)  # 读入内存
        # img = Image.open(img)  # PIL读取
        # img.show()

        start_inf = time.time()
        model = ONNXModel(name=model_choice, scale='small',
                          path_url="api/detection/onnx_ptw")
        out_dict = model.inference(input_url=store_file)
        time_cost = time.time() - start_inf
        for k in out_dict:  # 坐标向下取整
            out_dict[k] = list(map(int, out_dict[k]))
        print(len(out_dict), out_dict)

        os.remove(store_file)  # 删除存储的文件

        return Response(data={
            "pred": out_dict,
            "time": round(time_cost, 2)
        }, status=status.HTTP_200_OK)

        # if serializer.is_valid():
        #     print("登陆成功!")
        #     # from api.serializers.auth import jwt_generate
        #     # print(jwt_generate(payload={"name": "yoc", "password": "jwt"}))
        #     return Response(
        #         data={"data": serializer.data, "user": request.user}
        #     )
        # else:
        #     print("登录失败!")
        #     return Response(
        #         status=status.HTTP_404_NOT_FOUND
        #     )
