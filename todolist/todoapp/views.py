# todolist_app/views.py
from rest_framework import generics
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer
from .filters import TaskFilter


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    def perform_create(self, serializer):
        parent_task_id = self.kwargs["parent_task_id"]
        parent_task = Task.objects.get(pk=parent_task_id)
        serializer.save(parent_task=parent_task)


class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by("deadline")  # 締切順に整列
    serializer_class = TaskSerializer
    filterset_class = TaskFilter  # 検索機能追加

    def get_queryset(self):
        queryset = Task.objects.all()
        title = self.request.query_params.get("title", None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)  # 「__icontains」を追加する
        return queryset


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        serializer.save(parent_task=self.get_object())  # 更新時に子タスクを追加
