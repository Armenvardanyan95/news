from rest_framework import viewsets
from .serializers import MagazineSerializer, Magazine
from rest_framework.response import Response
from core.permissions import IsAuthenticated
from rest_framework import filters
from django.db.models import F


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all().order_by('randomizer')
    serializer_class = MagazineSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

    def retrieve(self, request, slug=None):

        Magazine.objects.filter(slug=slug).update(views=F('views')+1)
        if request.user.is_authenticated():
            Magazine.objects.filter(slug=slug).update(views=F('auth_views')+1)
        return super().retrieve(request, slug)


class MagazineSubscribeView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        request.user.magazines.add(Magazine.objects.get(slug=pk))

        return Response({'message': 'Successfully subscribed'})


class MagazineUnsubscribeView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        request.user.magazines.remove(Magazine.objects.get(slug=pk))

        return Response({'message': 'Successfully unsubscribed'})