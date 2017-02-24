from django.db import models
from utils.general import generate_randomizer
# from topics.models import Topic


class Magazine(models.Model):
    title = models.CharField(max_length=80, unique=True)
    admin = models.OneToOneField('accounts.User')
    description = models.TextField(max_length=1000)
    website = models.URLField(max_length=250)
    site_name = models.CharField(max_length=100)
    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    vk = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    main_pic = models.URLField()
    views = models.PositiveIntegerField(default=0)
    auth_views = models.PositiveIntegerField(default=0)
    article_views = models.PositiveIntegerField(default=0)
    limitation = models.IntegerField(default=100)
    slug = models.SlugField(unique=True)
    randomizer = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.randomizer = generate_randomizer(Magazine)
        super().save(force_insert=True)