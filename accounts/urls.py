from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'get-auth-token/$', views.GetAuthToken.as_view(), name='get-token-auth'),
]