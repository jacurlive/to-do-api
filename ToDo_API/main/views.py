from rest_framework import generics, permissions
from .models import ToDo, Folder
from .serializers import ToDoSerializer, ToDoDetailSerializer, FolderSerializer


# Get list and Create
class ToDoView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]


# Get detail and Update with pk
class ToDoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# Get list and Create folder
class FolderAPIView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]


# Read for Folder items
class FolderToDoAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk:
            try:
                folder = Folder.objects.get(pk=pk)
                return ToDo.objects.filter(folder=folder)
            except Folder.DoesNotExist:
                return Folder.objects.none()


class FolderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]
