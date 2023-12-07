from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
