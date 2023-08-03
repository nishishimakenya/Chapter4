# Generated by Django 4.2.1 on 2023-08-02 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0005_remove_task_parent_task_delete_subtask"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "parent_task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_tasks",
                        to="todoapp.task",
                    ),
                ),
            ],
        ),
    ]
