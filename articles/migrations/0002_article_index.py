# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-03 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='index',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
