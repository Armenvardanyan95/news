from django.db import models
from magazines.models import Magazine
from topics.models import Topic
from utils.general import generate_randomizer


class Article(models.Model):

    title = models.CharField(max_length=150)
    brief = models.CharField(max_length=250, blank=True)
    reference = models.URLField()
    image = models.URLField()
    magazine = models.ForeignKey(Magazine)
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
