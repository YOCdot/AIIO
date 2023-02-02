# ---*--- File Information ---*---
# @File       :  utils.py
# @Date&Time  :  2023-02-01, 18:33:36
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


import os
import json


def get_config(file_path: str) -> dict:

    if not os.path.exists(file_path):
        raise FileExistsError("File: `{}` not exists!".format(file_path))

    with open(file_path, 'r') as json_file:
        json_dict = json.load(json_file)

    return json_dict
