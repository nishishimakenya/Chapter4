# todolist_app/urls.py
from django.urls import path
from .views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    SubTaskListCreateView,
    SubTaskRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task-retrieve-update-destroy",
    ),
    path(
        "tasks/<int:parent_task_id>/subtasks/",
        SubTaskListCreateView.as_view(),
        name="subtask-list-create",
    ),
    path(
        "subtasks/<int:pk>/",
        SubTaskRetrieveUpdateDestroyView.as_view(),
        name="subtask-retrieve-update-destroy",
    ),
]
