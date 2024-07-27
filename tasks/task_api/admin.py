from django.contrib import admin
from django.contrib.admin import register

from task_api.models import Task


@register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Панель администратора для Задач."""

    list_display = ("name", "description", "status", "time_created")
    search_fields = ("name",)
    empty_value_display = "-пусто-"
