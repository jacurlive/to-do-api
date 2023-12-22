import django
import os
import random 
from faker import Faker


def generate_fake_data(num: int) -> None:
    from main.models import ToDo, Folder

    fake = Faker()

    for _ in range(num):
        folder_instance = Folder.objects.get(pk=random.randint(1, 2))
        
        todo = ToDo.objects.create(title=fake.name(), description=fake.text(), folder=folder_instance)
        todo.save()
        print(f"Created: {todo}")


if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

    django.setup()

    generate_fake_data(101)
