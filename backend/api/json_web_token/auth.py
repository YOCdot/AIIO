# ---*--- File Information ---*---
# @File       :  auth.py
# @Date&Time  :  2023-01-26, 17:28:21
# @Project    :  backend
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

import datetime

import jwt
from jwt import exceptions
from django.conf import settings


def jwt_generate(payload: dict, header: dict = None, expire: int = None, algorithm: str = "HS256",
                 salt: str = None) -> str:
    # 添加超时时间
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=3 if not expire else expire)  # 默认3分钟
    return jwt.encode(
        headers={"typ": "jwt", "alg": "HS256"} if not header else header,
        payload=payload,
        key=settings.SECRET_KEY if not salt else salt,
        algorithm=algorithm).decode("utf-8")


class JWTAuthentication(BaseAuthentication):
    """
        BaseAuthentication中的authenticate提供了三种返回值
            1 抛出异常, 则后续请求不再执行
            2 返回一个元组, (element1, element2), 此时认证通过
                element1提供给视图类中调用request.user
                element2提供给视图类中调用request.auth
            3 返回一个None, 查阅一下吧
    """

    def authenticate(self, request) -> tuple:
        # 获取token并判断其合法性
        token = request.META.get("HTTP_AUTHORIZATION")

        salt = settings.SECRET_KEY

        # payload = None
        try:  # token验证成功?
            payload = jwt.decode(jwt=token, key=salt, verify=True)
        except exceptions.ExpiredSignatureError:
            # token超时(失效)
            raise AuthenticationFailed(detail={"msg": "token已超时(失效)", "state": 0})
        except jwt.DecodeError:
            # token认证失败
            raise AuthenticationFailed(detail={"msg": "token认证失败", "state": 0})
        except jwt.InvalidTokenError:
            # token非法
            raise AuthenticationFailed(detail={"msg": "token非法", "state": 0})

        return payload, token


if __name__ == '__main__':
    key = "django-insecure-pz+e98#%pf=v=ctr3(xc6&$@($-m_7-@c!tzym!qkoh(&*7bfc"
    token_gen = jwt_generate(
        payload={
            "adminname": "yoc",
        },
        salt=key
    )
    print(token_gen)

    token_decoded = jwt.decode(jwt=token_gen, key=key, verify=True)
    print(token_decoded)

    js = ""
    py = "eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9." \
         "eyJhZG1pbm5hbWUiOiJ5b2MiLCJleHAiOjE2NzUyNjAxNzV9." \
         "t9vRZWm9UV_KRZlVOu-C4Po7sbnPUzHOdRo7fyY0vjg"
    print("match" if js == py else "unmatch")
