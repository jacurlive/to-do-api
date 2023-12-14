from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user) -> Token:

        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username

        return super().get_token(user)
