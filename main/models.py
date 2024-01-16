from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self) -> models.CharField:
        return self.name


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> models.CharField:
        return self.title
