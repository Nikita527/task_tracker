from rest_framework import serializers

from task_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач."""

    class Meta:
        model = Task
        fields = ("id", "name", "description", "status", "time_created")
