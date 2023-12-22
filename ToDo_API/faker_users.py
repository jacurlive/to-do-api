import django
import os
import random 
from faker import Faker
from django.db import IntegrityError


def generate_fake_users(num: int) -> None:
    from user.models import User

    fake = Faker()

    for _ in range(num):

        username = fake.name()

        while True:
            try:
                user = User.objects.create(username=username, phone=fake.phone_number(), email="test@test.com", password=fake.password(length=8))
                user.save()
                print(f"Created: {user}")
                break
            except IntegrityError:
                username = fake.name()


if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

    django.setup()

    generate_fake_users(101)
