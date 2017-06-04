from django.db import models
from core.utils import Utilities

from topics.models import Topic
from utils.general import generate_randomizer

ARTICLE_TYPES = (
    ('article', 'Հոդված',),
    ('news', 'Նորություն')
)


class Article(models.Model):

    title = models.CharField(max_length=150)
    brief = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=50, choices=ARTICLE_TYPES)
    reference = models.URLField()
    image = models.URLField()
    magazine = models.ForeignKey("magazines.Magazine")
    topics = models.ManyToManyField(Topic)
    randomizer = models.PositiveIntegerField()
    index = models.PositiveIntegerField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_magazine_details(self):
        return {
            'id': self.magazine.id,
            'title': self.magazine.title,
            'main_pic': self.magazine.main_pic,
            'website': self.magazine.website,
            'site_name': self.magazine.site_name,
            'slug': self.magazine.slug,
        }

    @property
    def get_topics(self):
        return self.topics.values('id', 'title')

    def save(self, **kwargs):
        self.randomizer = generate_randomizer(Article)
        super().save(force_insert=True)


class SavedArticle(models.Model):

    user = models.ForeignKey("accounts.User")
    article = models.ForeignKey(Article)
    save_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_article(self):
        article = Utilities.to_dict(self.article)
        return article

