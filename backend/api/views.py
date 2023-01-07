from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet  # 视图集 - ViewSet
from rest_framework.decorators import action  # 动作装饰器 (装饰类内方法令路由进行注册)

from api.models import Links
from api.serializers import LinksModelSerializer

from api.detection import ONNXModel


class TestView(APIView):
    """ 测试视图 """
    def get(self, request):

        return Response("testing...")


class LinksModelViewSet(ModelViewSet):
    """ 个人链接视图集 """

    # 必要的属性
    queryset = Links.objects.all()
    serializer_class = LinksModelSerializer

    # # 获取所有个人链接 - 只有列表视图
    # def list(self, request):
    #     queryset = self.queryset
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # # 修改 `pk=1` 的对象的阅读量为 `99`
    # @action(methods=["PUT"], detail=True)  # 动作装饰 - 路由生成规则: <prefix/{pk}/method_name> - detail=True: 表示详情视图
    # def bread_update(self, request, pk):
    #     # 获取对象
    #     book = self.get_object()
    #     data = request.data
    #
    #     # 序列化器
    #     serializer = self.get_serializer(instance=book, data=data, partial=True)  # partial=True 即为 PATCH 请求
    #
    #     # 校验 + 入库
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
