# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200709_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, db_index=True),
        ),
    ]
