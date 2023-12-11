from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer


# Get list and Create
class ToDoView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


# Get detail and Delete with pk
class ToDoDestroy(generics.RetrieveDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


# Update
# class ToDoUpdate(generics.UpdateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer


# Get detail and Update with pk
class ToDoDetail(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
