import os
import django
import random 
from .models import ToDo
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

fake = Faker()


def generate_fake_data(num: int) -> None:
    for _ in range(num):

        ToDo.objects.create(title=fake.title(), description=fake.description(), folder=random.randint(1, 3))


generate_fake_data(101)
