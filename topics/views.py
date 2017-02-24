from rest_framework.viewsets import ModelViewSet, ViewSet
from accounts.models import User
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all().order_by('randomizer')
    serializer_class = TopicSerializer
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'keywords',)
    ordering_fields = ('?',)


class TopicSubscribeView(ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        request.user.topics.add(Topic.objects.get(id=pk))

        return Response({'message': 'Successfully subscribed'})


class TopicUnsubscribeView(ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        request.user.topics.remove(Topic.objects.get(id=pk))

        return Response({'message': 'Successfully unsubscribed'})



