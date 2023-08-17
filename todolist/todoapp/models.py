# todolist_app/models.py
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=200)
    parent_task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="sub_tasks"
    )  # 親タスクからsub_tasks でアクセス可能、on_deleteでサブタスクも同時に削除

    def __str__(self):
        return self.title
