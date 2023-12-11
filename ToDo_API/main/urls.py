from django.urls import path
from .views import ToDoView, ToDoDestroy, ToDoDetail, FolderAPIView


urlpatterns = [
    path('todo/', ToDoView.as_view()), # Read and Create
    path('todo/delete/<int:pk>/', ToDoDestroy.as_view()), # Delete and Read
    path('todo/detail/<int:pk>/', ToDoDetail.as_view()), # Update and Read
    path('folder/', FolderAPIView.as_view()) # Read and Create
]
