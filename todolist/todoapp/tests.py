from datetime import datetime
from django.utils.timezone import make_aware
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_task(self):
        deadline = make_aware(datetime(2023, 8, 31, 15, 55))
        response = self.client.post(
            "/api/tasks/", {"title": "Test Task", "deadline": deadline, "memo": "aiueo"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_task_by_title(self):
        deadline = make_aware(datetime(2023, 8, 31, 15, 55))
        task = Task.objects.create(
            title="Search Test Task", deadline=deadline, memo="aiueo"
        )
        response = self.client.get("/api/tasks/", {"title": "Search Test Task"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], task.title)
