# ---*--- File Information ---*---
# @File       :  jwt_serializers.py
# @Date&Time  :  2023-02-01, 22:28:38
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from api.models import Admin


class JWTSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        pass
