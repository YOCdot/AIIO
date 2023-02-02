# ---*--- File Information ---*---
# @File       :  __init__.py.py
# @Date&Time  :  2023-02-01, 21:44:14
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from django import forms

from api.models import Admin


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ["adminname", "password"]
