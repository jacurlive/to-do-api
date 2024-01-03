from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self) -> str:
        return self.name


class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
