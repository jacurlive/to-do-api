from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
