# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200709_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='maxResolution',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
