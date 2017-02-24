from django.db import models
from accounts.models import User
from articles.models import Article


class BasicView(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)


class UserView(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.user.first_name + ': ' + self.article.title + '(' + str(self.time) + ')'


class Share(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.user.first_name + ': ' + self.article.title + '(' + str(self.time) + ')'


