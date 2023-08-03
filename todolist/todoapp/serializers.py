# todolist_app/serializers.py
from rest_framework import serializers
from .models import Task, SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ["id", "title", "parent_task"]


class TaskSerializer(serializers.ModelSerializer):
    sub_tasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "deadline", "memo", "sub_tasks"]
