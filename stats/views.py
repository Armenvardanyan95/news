from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from core.permissions import IsMagazineAdmin
from rest_framework.response import Response
from django.db.models import F
from .models import UserView, BasicView, Share
from articles.models import Article


class UserViewArticleViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def retrieve(self, request, pk, format=None):
        article = Article.objects.get(pk=pk)
        Article.objects.filter(pk=pk).update(views=F('views') + 1)
        UserView.objects.create(user=request.user, article=article)

        return Response({'message': 'Successfully logged'})


class BasicViewArticleViewSet(ViewSet):
    http_method_names = ['get']

    def retrieve(self, request, pk, format=None):
        article = Article.objects.get(pk=pk)
        Article.objects.filter(pk=pk).update(views=F('views') + 1)
        BasicView.objects.create(article=article)

        return Response({'message': 'Successfully logged'})


class ShareViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def retrieve(self, request, pk, format=None):
        article = Article.objects.get(pk=pk)
        if Share.objects.filter(article=article, user=request.user).exists():
            return Response({'message': 'Already shared'})

        Share.objects.create(article=article, user=request.user)

        return Response({'message': 'Successfully logged'})


class StatisticsViewSet(ViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, IsMagazineAdmin)
    http_method_names = ['get']

    def list(self, *args, **kwargs):
        magazine = self.request.user.magazine
        shares_count = Share.objects.filter(article__magazine=magazine).count()
        last_month_article_views_by_auth_users = UserView.objects.filter(article__magazine=magazine).count() +\
                                                 BasicView.objects.filter(article__magazine=magazine).count()
        subscribers = magazine.user_set.count()

        return Response({'shares_count': shares_count,
                         'magazine_views': magazine.views,
                         'magazine_auth_views': magazine.auth_views,
                         'last_month_article_views_by_auth_users': last_month_article_views_by_auth_users,
                         'number_of_subscribers': subscribers
                         })
