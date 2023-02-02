from django.db import models


class Links(models.Model):
    """ 链接表 """
    title = models.CharField(verbose_name="名称", max_length=32)
    link = models.CharField(verbose_name="链接网址", max_length=192)
    # 本质上在数据库中也还是 CharField，但django能自动保存
    icon = models.ImageField(verbose_name="icon", upload_to='links/')  # 直接传到 media/links/


class Admin(models.Model):
    """ 管理员表 """
    adminname = models.CharField(verbose_name="管理员", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=256)

    def __str__(self):
        return "Admin - {}".format(self.adminname)


class User(models.Model):
    """ 用户表 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=32)
    ctime = models.DateTimeField(verbose_name="创建时间")  # 设计不够合理，时分秒较为多余


class Detections(models.Model):
    """ 目标检测表 """
    instance = models.CharField(verbose_name="名称", max_length=32)
    # 本质上在数据库中也还是 CharField，但django能自动保存
    image = models.ImageField(verbose_name="检测图", upload_to='detections/')  # 直接传到 media/detections/
    results = models.TextField(verbose_name="检测结果JSON")
