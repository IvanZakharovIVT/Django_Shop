# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_post_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
