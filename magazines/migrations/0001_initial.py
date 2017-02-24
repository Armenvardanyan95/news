# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-02 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('website', models.URLField(max_length=250)),
                ('facebook', models.CharField(blank=True, max_length=250)),
                ('twitter', models.CharField(blank=True, max_length=250)),
                ('vk', models.CharField(blank=True, max_length=250)),
                ('instagram', models.CharField(blank=True, max_length=250)),
                ('main_pic', models.URLField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('article_views', models.PositiveIntegerField(default=0)),
                ('limitation', models.IntegerField(default=100)),
                ('slug', models.SlugField(unique=True)),
                ('randomizer', models.PositiveIntegerField()),
            ],
        ),
    ]