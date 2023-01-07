# ---*--- File Information ---*---
# @File       :  serializers.py
# @Date&Time  :  2023-01-07, 00:26:19
# @Project    :  AIIO
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from rest_framework import serializers

from api.models import Links, Admin, User, Detections


class LinksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"


class DetectionsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detections
        fields = "__all__"


class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
