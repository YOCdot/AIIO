# ---*--- File Information ---*---
# @File       :  urls.py
# @Date&Time  :  2023-01-07, 00:09:41
# @Project    :  AIIO
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views


urlpatterns = [

    # """ 使用路由实例进行代替 """

    # path("books/", views.BookInfoModelViewSet.as_view({"get": "list",
    #                                                    "post": "create"})),
    # path("books/<int:pk>/", views.BookInfoModelViewSet.as_view({"get": "retrieve",
    #                                                             "put": "update",
    #                                                             "delete": "destroy"})),
    # path("books/bread/gt/", views.BookInfoModelViewSet.as_view({"get": "bread_books"})),
    # path("books/bread/<int:pk>/", views.BookInfoModelViewSet.as_view({"put": "bread_update"})),

    path("test/", views.TestView.as_view()),
]

# 1. 创建路由对象
# router = DefaultRouter()
router = SimpleRouter()

# 2. 注册视图集
router.register(prefix="links", viewset=views.LinksModelViewSet, basename="links")
urlpatterns += router.urls

# 3. 输出结果
# print(urlpatterns)


"""
Routers 路由
    - 只能配合 `ViewSet` 进行使用

可以通过请求头`Headers`来请求不同类型的数据
    - application/json: 序列化 json 数据
    - text/html: drf raw 数据

DefaultRouter - 自动添加 json raw 的 url
    - 自动生成 `list/detail`
    [
        # 列表视图 (name='`basename`-list')
        <URLPattern '^books/$' [name='books-list']>,  # 序列化json
        <URLPattern '^books\.(?P<format>[a-z0-9]+)/?$' [name='books-list']>,  # json raw (自动添加)

        # 详情视图 (name='`basename`-detail')
        <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='books-detail']>,  # 序列化json
        <URLPattern '^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='books-detail']>,  # json raw (自动添加)

        # 根路由 (引导)
        <URLPattern '^$' [name='api-root']>,
        <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
    ]

SimpleRouter - 不添加 json raw 的url
    - 自动生成 `list/detail`
    [
        <URLPattern '^books/$' [name='books-list']>,
        <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='books-detail']>
    ]
"""
