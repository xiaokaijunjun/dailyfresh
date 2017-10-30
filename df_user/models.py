from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20,verbose_name='用户名')
    upwd = models.CharField(max_length=40,verbose_name='密码')
    uemail = models.CharField(max_length=30,verbose_name='邮箱')
    ushou = models.CharField(max_length=20,default='',verbose_name='收件人')
    uaddress = models.CharField(max_length=100,default='',verbose_name='地址')
    uyoubian = models.CharField(max_length=6,default='',verbose_name='邮编')
    uphone = models.CharField(max_length=11,default='',verbose_name='手机')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.uname