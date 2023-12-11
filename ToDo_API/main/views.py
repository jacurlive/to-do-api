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


# Read for Folder items
class FolderToDoAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk:
            try:
                folder = Folder.objects.get(pk=pk)
                return ToDo.objects.filter(folder=folder)
            except Folder.DoesNotExist:
                return Folder.objects.none()
