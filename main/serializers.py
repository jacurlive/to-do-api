from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ToDo, Folder


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = ToDo
        fields = "__all__"
        read_only_fields = ("user",)

    def get_user(self, obj):
        return obj.user.username


# class ToDoDetailSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()

#     class Meta:
#         model = ToDo
#         fields = "__all__"
#         read_only_fields = ("user",)

    
#     def get_user(self, obj):
#         return obj.user.username
