from django.urls import path
from .views import ToDoView, ToDoDestroy, ToDoUpdate, ToDoDetail


urlpatterns = [
    path('todo/', ToDoView.as_view()),
    path('todo/<int:pk>/', ToDoUpdate.as_view()),
    path('todo/delete/<int:pk>/', ToDoDestroy.as_view()),
    path('todo/detail/<int:pk>/', ToDoDetail.as_view())
]
