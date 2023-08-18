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
    # リスト取得と作成
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task-retrieve-update-destroy",
    ),
    # 詳細情報の取得と更新、削除
    path(
        "tasks/<int:parent_task_id>/subtasks/",
        SubTaskListCreateView.as_view(),
        name="subtask-list-create",
    ),
    # 特定の親タスクに関連するサブタスクのリストの取得と作成
    path(
        "subtasks/<int:pk>/",
        SubTaskRetrieveUpdateDestroyView.as_view(),
        name="subtask-retrieve-update-destroy",
    ),
    # 特定のサブタスクの編集
]
