# todoapp/filters.py
import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            "title": ["exact", "icontains"],
            "deadline": ["exact", "lte", "gte"],
        }
#あまり理解できていない
#next editting
#今日はfilters.py