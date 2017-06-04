from core.tests import BaseTest
from django.core.urlresolvers import reverse
from .models import Topic
from .serializers import TopicSerializer
from rest_framework import status


class TopicAPI(BaseTest):

    serializer_class = TopicSerializer
    valid_data = {'title': 'test_title'};

    def test_create_topic(self):
        url = reverse('topic-list')
        data = {'title': 'test_title'}
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Topic.objects.count(), 1)
        self.assertEqual(Topic.objects.all().first().title, 'test_title')

    def test_invalid_creation(self):
        url = reverse('topic-list')
        data = {'title': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_list_topics(self):
        # self.__fillData()
        url = reverse('topic-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, )

