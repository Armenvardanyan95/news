from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=50, blank=False)
    subscribers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

class Magazine(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.TextField(max_length=1000)
    topics = models.ManyToManyField(Topic)
    website = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    vk = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    main_pic = models.ImageField(upload_to='magazines')
    views = models.IntegerField()
    article_views = models.IntegerField()
    subscribers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=150)
    brief = models.CharField(max_length=250)
    reference = models.URLField()
    image = models.ImageField(upload_to='articles')
    magazine = models.ForeignKey(Magazine)
    topics = models.ManyToManyField(Topic)
    views = models.IntegerField()

    def __str__(self):
        return self.title