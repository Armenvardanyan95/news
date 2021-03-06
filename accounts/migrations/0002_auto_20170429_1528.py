# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('magazines', '0001_initial'),
        ('topics', '0001_initial'),
        ('accounts', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='magazines',
            field=models.ManyToManyField(blank=True, to='magazines.Magazine'),
        ),
        migrations.AddField(
            model_name='user',
            name='topics',
            field=models.ManyToManyField(blank=True, null=True, to='topics.Topic'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
