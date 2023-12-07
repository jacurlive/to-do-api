from django.shortcuts import render
from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
