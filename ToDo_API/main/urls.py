from django.urls import path
from .views import ToDoView


urlpatterns = [
    path('api/v1/todo', ToDoView.as_view())
]
