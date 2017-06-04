from django.db import models
from utils.general import generate_randomizer


class Topic(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    keywords = models.TextField()
    related_topics = models.ManyToManyField('self', blank=True)
    abbr_arm = models.CharField(max_length=200, blank=True)
    abbr_eng = models.CharField(max_length=200, blank=True)
    title_eng = models.CharField(max_length=200, blank=False)
    randomizer = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.randomizer = generate_randomizer(Topic)
        super().save(force_insert=True)
