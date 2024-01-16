from rest_framework.test import APITestCase
from rest_framework import status
from .models import Folder


class FolderAPITest(APITestCase):
    def test_create_folder(self):
        response = self.client.post('/todo/folder/', {"name": "test"})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
