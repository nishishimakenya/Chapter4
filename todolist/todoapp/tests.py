from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_task(self):
        response = self.client.post('/tasks/', {'title': 'Test Task', 'deadline': '2023-08-31 15:55'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_task_by_title(self):
        task = Task.objects.create(title='Search Test Task', deadline='2023-08-31 15:55')
        response = self.client.get('/tasks/', {'title': 'Search Test Task'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], task.title)
