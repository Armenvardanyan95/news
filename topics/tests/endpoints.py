from django.test import TestCase
from topics.models import Topic
from rest_framework.test import APIClient

client = APIClient(force_authenticate=True)


class TopicTestCase(TestCase):

    def setUp(self):
        Topic.objects.create(title='Ֆուտբոլ')
        Topic.objects.create(title='Թենիս')