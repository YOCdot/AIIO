# ---*--- File Information ---*---
# @File       :  detection.py
# @Date&Time  :  2023-02-01, 16:29:26
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet  # 视图集 - ViewSet
from rest_framework.decorators import action  # 动作装饰器 (装饰类内方法令路由进行注册)


from api.models import Links, Admin
from api.serializers.model_serializers import LinksModelSerializer, AdminModelSerializer

from api.detection import ONNXModel
