from rest_framework.viewsets import ModelViewSet, ViewSet
# from accounts.models import User
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicRetrieveSerializer, TopicListSerializer
from rest_framework import filters
from core.permissions import IsAuthenticated


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all().order_by('randomizer')
    serializer_class = TopicRetrieveSerializer
    # permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'keywords', 'abbr_arm', 'abbr_eng', 'title_eng',)
    ordering_fields = ('?',)

    def list(self, request, *args, **kwargs):
        self.serializer_class = TopicListSerializer
        return super().list(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TopicRetrieveSerializer
        return super().retrieve(request, args, kwargs)

    def get_queryset(self):
        return self.queryset if not (self.request.GET.get('not_mine') and self.request.user.is_authenticated()) else self.queryset.exclude(id__in=self.request.user.topics.values('id'))

class TopicSubscribeView(ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        topic = Topic.objects.get(id=pk)
        if topic not in request.user.topics.all():
            request.user.topics.add(topic)
        else:
            request.user.topics.remove(topic)

        return Response({'message': 'Successfully subscribed'})


class TopicUnsubscribeView(ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        request.user.topics.remove(Topic.objects.get(id=pk))

        return Response({'message': 'Successfully unsubscribed'})



