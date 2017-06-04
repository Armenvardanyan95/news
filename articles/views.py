from rest_framework import viewsets
import urllib.request as urllib
from rest_framework.viewsets import ViewSet
from bs4 import BeautifulSoup
from rest_framework import status
from core.permissions import IsAuthenticated
from .models import Article
from stats.models import UserView
from .serializers import ArticleSerializer
from rest_framework import filters
from rest_framework.response import Response


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().select_related('magazine').prefetch_related('topics')
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)
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


class ParseArticleViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, format=None):

        url = request.GET.get("url", None)
        if not url:
            return Response({"message": "No URL given"})

        # try:
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML,'
                          ' like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }
        req = urllib.Request(url=url, headers=hdr)
        page = urllib.urlopen(req)
        page = BeautifulSoup(page, "html.parser")
        images = []
        for img in page.find_all("img"):
            images.append(img.get("src"))
        return Response({
            "title": page.title.get_text(),
            "images": images
        })

        # except:
        #     return Response({"message": "Could not parse page"}, status=status.HTTP_404_NOT_FOUND)



>>>>>>> Changes
