from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import User


class GetAuthToken(ObtainAuthToken):
    """
    ---
    POST:
          serializer: AuthTokenSerializer
    OPTIONS:
          serializer: AuthTokenSerializer
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user = User.objects.get(username=user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': user.id })


class UsersViewSet(ModelViewSet):

    queryset = User.objects.filter()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'options']
    permission_classes = [AllowAny]
