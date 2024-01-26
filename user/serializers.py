from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(min_length=8, max_length=32, write_only=True)
    email = serializers.EmailField(allow_blank=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user = User(username=username, email=email, is_active=False)
        user.set_password(password)
        user.save()
        return user
