# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='index',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
