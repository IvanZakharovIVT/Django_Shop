# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'draft', max_length=10, db_index=True, choices=[(b'draft', b'Draft'), (b'published', b'Published')]),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
