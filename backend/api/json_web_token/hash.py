# ---*--- File Information ---*---
# @File       :  hash.py
# @Date&Time  :  2023-01-26, 17:28:13
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


import jwt
import json
import hashlib
from django.conf import settings


class JWTCypher:
    """
    `HASH` 加密
    """

    def __init__(self,
                 payload: dict,
                 header: dict = None,
                 alg: str = "sha256",
                 secret: str = None,
                 use_default: bool = True):
        super().__init__()

        self.content = json.dumps(payload)
        self.secret = secret
        self.use_default = use_default

        if not header:
            header = {

            }

        if alg not in ["sha256", "md5"]:
            raise KeyError(f"没有提供这种加密方法`{alg}`")
        self.alg = eval("hashlib." + alg + "()")

    def encrypt(self):

        # m.update(a); m.update(b) 等价于 m.update(a+b)
        self.alg.update(self.content.encode("utf-8"))

        if self.use_default:
            # pass
            self.alg.update(settings.SECRET_KEY.encode("utf-8"))
        elif self.secret:
            self.alg.update(self.secret)

        return self.alg.hexdigest()


if __name__ == '__main__':
    raw_payload = {
        "name": "yoc",
        "password": "jwt"
    }
    cypher = JWTCypher(payload=raw_payload, use_default=False)

    print(cypher.encrypt())
