from django.urls import path
from .views import ToDoView, ToDoDestroy, ToDoDetail, FolderAPIView, FolderToDoAPIView


urlpatterns = [
    path('todo/', ToDoView.as_view()), # Read and Create todo
    path('todo/delete/<int:pk>/', ToDoDestroy.as_view()), # Delete and Read todo
    path('todo/detail/<int:pk>/', ToDoDetail.as_view()), # Update and Read todo
    path('folder/', FolderAPIView.as_view()), # Read and Create folder
    path('folder/<int:pk>/', FolderToDoAPIView.as_view()) # Read for folder items
]
