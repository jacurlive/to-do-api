from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    password2 = models.CharField(max_length=155, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
