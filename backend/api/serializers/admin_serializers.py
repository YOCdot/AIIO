# ---*--- File Information ---*---
# @File       :  admin_serializers.py
# @Date&Time  :  2023-02-01, 22:23:20
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from rest_framework import serializers

from api.models import Admin


class AdminSerializer(serializers.Serializer):

    adminname = serializers.CharField(label="管理员", max_length=32)
    password = serializers.CharField(label="密码", max_length=256)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        """
        attrs: real value - OrderedDict([('adminname', 'yoc'), ('password', '465465464564654564')])
        """

        query = Admin.objects.get(adminname=attrs["adminname"])

        if attrs["password"] == query.password:
            return attrs
        else:
            return {"msg": "密码错误!"}


