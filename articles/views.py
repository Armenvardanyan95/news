from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Article
from stats.models import UserView
from .serializers import ArticleSerializer
from rest_framework import filters
from rest_framework.response import Response


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().select_related('magazine').prefetch_related('topics')
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('topics', 'magazine')
    ordering_fields = ('created', 'views',)


class ArticleByTopicViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all().select_related('magazine').prefetch_related('topics', ).order_by('randomizer')
    http_method_names = ['get']
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return self.queryset.filter(topics__in=self.request.user.topics.all()).exclude(
            id__in=UserView.objects.filter(user=self.request.user).values('article')
        )


class ArticleByMagazineViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    http_method_names = ['get']
    queryset = Article.objects.all().order_by('randomizer')

    def get_queryset(self):
        return self.queryset.filter(magazine__in=self.request.user.magazines.all()).exclude(
            id__in=UserView.objects.filter(user=self.request.user).values('article')
        )


class ArticleHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    http_method_names = ['get']
    queryset = Article.objects.all().order_by('created')

    def get_queryset(self):
        return self.queryset.filter(id__in=UserView.objects.filter(user=self.request.user).values('article'))


class SaveArticleViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk, format=None):
        request.user.saved_articles.add(Article.objects.get(id=pk))

        return Response({'message': 'Sucessfully saved'})
