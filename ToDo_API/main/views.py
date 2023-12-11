from rest_framework import generics, permissions
from .models import ToDo, Folder
from .serializers import ToDoSerializer, FolderSerializer


# Get list and Create
class ToDoView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]


# Get detail and Delete with pk
class ToDoDestroy(generics.RetrieveDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]


# Get detail and Update with pk
class ToDoDetail(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]


class FolderAPIView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]
