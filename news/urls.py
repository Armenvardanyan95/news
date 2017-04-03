from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from topics.views import TopicViewSet, TopicSubscribeView, TopicUnsubscribeView
from magazines.views import MagazineViewSet, MagazineSubscribeView, MagazineUnsubscribeView
from articles.views import ArticleViewSet, ArticleByTopicViewSet, ArticleByMagazineViewSet, ArticleHistoryViewSet,\
    SaveArticleViewSet, ParseArticleViewSet, BulkHistory
from accounts.views import UsersViewSet, GetAuthToken
from stats.views import UserViewArticleViewSet, ShareViewSet, StatisticsViewSet


router = routers.DefaultRouter()

router.register('topics', TopicViewSet)
router.register('topics/unsubscribe', TopicUnsubscribeView, base_name='unsubscribe')
router.register('topics/subscribe', TopicSubscribeView, base_name='topics/subscribe')
router.register('magazines', MagazineViewSet)
router.register('magazines/subscribe', MagazineSubscribeView, base_name='magazines/subscribe')
router.register('magazines/unsubscribe', MagazineUnsubscribeView, base_name='magazines/unsubscribe')
router.register('articles', ArticleViewSet)
router.register('articles/custom/by-topic', ArticleByTopicViewSet, base_name='articles/custom/by-topic')
router.register('articles/custom/by-magazine', ArticleByMagazineViewSet, base_name='articles/custom/by-magazine')
router.register('articles/custom/history', ArticleHistoryViewSet, base_name='articles/custom/history')
router.register("bulk-history", BulkHistory, base_name="bulk-history")
router.register('articles/save', SaveArticleViewSet, base_name='articles/save')
router.register('users', UsersViewSet)
router.register('parse', ParseArticleViewSet, base_name='parse')
router.register('stats-auth', UserViewArticleViewSet, base_name='stats-auth')
router.register('statistics', StatisticsViewSet, base_name='statistics')
router.register('share', ShareViewSet, base_name='share')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'get-auth-token/$', GetAuthToken.as_view(), name='get-auth-token'),
]
