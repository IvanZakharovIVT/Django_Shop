# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_auto_20200708_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date=b'publish')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'published', b'Published')])),
                ('author', models.ForeignKey(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='maxExcerpt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='maxResolution',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='megapixels',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'products', blank=True),
        ),
    ]
