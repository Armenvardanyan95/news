from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from topics.models import Topic
from magazines.models import Magazine
from articles.models import Article

from rest_framework.authtoken.models import Token


class User(AbstractUser):

    token = models.CharField(null=True, blank=True, max_length=255)
    topics = models.ManyToManyField(Topic, null=True, blank=True)
    magazines = models.ManyToManyField(Magazine, blank=True)
    saved_articles = models.ManyToManyField(Article, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.username = self.email
        return super(User, self).save(force_insert, force_update, using, update_fields)

    @property
    def magazine(self):
        return Magazine.objects.filter(admin=self).first()

    def __unicode__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

