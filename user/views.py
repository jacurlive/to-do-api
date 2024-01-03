from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import generics


User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
