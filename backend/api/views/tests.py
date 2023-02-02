# ---*--- File Information ---*---
# @File       :  tests.py
# @Date&Time  :  2023-02-01, 16:29:08
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView  # 二级视图

from api.models import Admin
from api.forms import AdminForm
from api.serializers import AdminModelSerializer
from api.json_web_token.auth import jwt_generate, JWTAuthentication


class TestView(APIView):
    """ 测试视图 """
    def get(self, request):

        return Response("testing...")


class LoginTest(GenericAPIView):

    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer

    def get(self, request):
        return Response(data={"msg": "请登陆!"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):

        form_data = request.data
        print(form_data)

        # 使用刚刚编写时序列化处理登陆验证及数据响应
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f'验证失败： {e}')

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ApiTest(GenericAPIView):

    authentication_classes = [JWTAuthentication, ]
    queryset = Admin.objects.all()
    lookup_field = "adminname"

    def get(self, request):
        return Response(data={"msg": "success!"})



# class LoginTest(views.TokenObtainPairView):
#     # serializer_class = LoginTestSerializer
#     # serializer_class = AdminModelSerializer
#     serializer_class = AdminSerializer
#
#     def get(self, request):
#         # 通过request.auth获取用户Token
#         print('请求用户Token为：')
#         print(request.auth)
#
#         # 通过request.auth.payload可以获取到解析后的payload内容（字典类型）
#         print("\n有效荷载信息：")
#         print(request.auth.payload)
#
#         return Response('身份验证通过！', status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         # 使用刚刚编写时序列化处理登陆验证及数据响应
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             raise ValueError(f'验证失败： {e}')
#
#         return Response(serializer.validated_data, status=status.HTTP_200_OK)
