from rest_framework import generics, permissions
from .models import ToDo, Folder
from .pagination import PostLimitOffsetPagination
from .serializers import ToDoSerializer, ToDoDetailSerializer, FolderSerializer
from .permissions import IsOwner


# Get list and Create
class ToDoView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoDetailSerializer
    permission_classes = [IsOwner]
    pagination_class = PostLimitOffsetPagination

    def get_serializer_context(self):
        return {"request": self.request}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
    pagination_class = PostLimitOffsetPagination

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
