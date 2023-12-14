from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()


    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        


class PlainTextField(models.TextField):
    def get_prep_value(self, value):
        return value

class User(AbstractUser):
    phone = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    password = PlainTextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
