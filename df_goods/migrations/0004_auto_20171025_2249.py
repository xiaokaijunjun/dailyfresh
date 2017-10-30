# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-25 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0003_auto_20171025_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeinfo',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='typeinfo',
            name='isDelete',
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gadv',
            field=models.BooleanField(default=False, verbose_name='是否推荐'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(verbose_name='点击量'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gdescript',
            field=models.CharField(max_length=200, verbose_name='商品描述'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='goods', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gstock',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default='500g', max_length=20, verbose_name='数量'),
        ),
    ]