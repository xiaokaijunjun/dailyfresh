from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20,verbose_name='分类')
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20,verbose_name='商品名称')
    gpic = models.ImageField(upload_to='goods',verbose_name='商品图片')
    gprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格',default=20.00)
    gunit = models.CharField(max_length=20,default='500g',verbose_name='数量')
    gclick = models.IntegerField(verbose_name='点击量',default=1000)
    gdescript = models.CharField(max_length=200,verbose_name='商品描述')    #商品描述
    gstock = models.IntegerField(verbose_name='库存',default=500)                  #库存
    gcontent = HTMLField()                          #商品详情
    gtype = models.ForeignKey(TypeInfo,to_field='id')
    gcom = models.BooleanField(default=False,verbose_name='是否推荐')       #推荐

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.gtitle

class AdvInfo(models.Model):
    apic = models.ImageField(upload_to='adv',verbose_name='广告图片')
    acom = models.BooleanField(default=False,verbose_name='是否推荐')
    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name