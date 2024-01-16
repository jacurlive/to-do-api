from django.urls import path

from .views import ToDoView, ToDoDetailAPIView, FolderAPIView, FolderToDoAPIView, FolderDetailAPIView

urlpatterns = [
    path('', ToDoView.as_view()),  # Read and Create todo
    path('<int:pk>/', ToDoDetailAPIView.as_view()),  # Update, Delete and Read todo
    path('folder/', FolderAPIView.as_view()),  # Read and Create folder
    path('folder/<int:pk>/', FolderToDoAPIView.as_view()),  # Read for folder items
    path('folder/detail/<int:pk>/', FolderDetailAPIView.as_view())  # Update, Delete and Read folders
]
