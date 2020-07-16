# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_post_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'published', b'Published')]),
        ),
    ]
