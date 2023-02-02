# ---*--- File Information ---*---
# @File       :  admin.py
# @Date&Time  :  2023-02-01, 16:28:56
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet  # 视图集 - ViewSet
from rest_framework.decorators import action  # 动作装饰器 (装饰类内方法令路由进行注册)

from api.models import Links, Admin
from api.serializers.model_serializers import LinksModelSerializer, AdminModelSerializer
from api.serializers import AdminSerializer
from api.json_web_token import jwt_generate, JWTAuthentication


class AccessToken(APIView):

    def post(self, request):
        adminname = request.data.get("adminname")
        password = request.data.get("password")
        # print(request.data)
        # print(request.user)
        # print(request.auth)

        serializer = AdminSerializer(data=request.POST)
        result = serializer.is_valid(raise_exception=True)

        query = Admin.objects.get(adminname=adminname)
        if query and password == query.password:

            token = jwt_generate(payload={"adminname": adminname})
            print("generated:", token)

            data = {
                "msg": "登陆成功",
                "stat": 1,
                "Access Token": token
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={"msg": "密码错误/没有此账户"}, status=status.HTTP_401_UNAUTHORIZED)


class ApiTest(APIView):

    authentication_classes = [JWTAuthentication, ]

    def get(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        print("ok:", token)
        return Response(data={"user": request.user, "auth": request.auth}, status=200)


class AdminLogin(APIView):
    """ 管理员登陆 """

    def post(self, request):

        # print(request.data)

        serializer = AdminModelSerializer(data=request.data)
        if serializer.is_valid():
            print("登陆成功!")
            # from api.serializers.auth import jwt_generate
            # print(jwt_generate(payload={"name": "yoc", "password": "jwt"}))
            return Response(
                data={"data": serializer.data, "user": request.user}
            )
        else:
            print("登录失败!")
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
