# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200712_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='product',
            field=models.ForeignKey(related_name='blog_posts', blank=True, to='shop.Product', null=True),
        ),
    ]
