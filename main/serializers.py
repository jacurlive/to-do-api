from rest_framework import serializers
from .models import ToDo, Folder


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ("id", "title", "completed", "user")
        read_only_fields = ("user",)


class ToDoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
        read_only_fields = ("user",)
