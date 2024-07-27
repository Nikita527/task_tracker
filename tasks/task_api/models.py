from elasticsearch_dsl import Date, Document, Text, connections

from django.conf import settings
from django.db import models

STATUS_CHOICES = [
    ("queued", "В очереди"),
    ("in_progress", "В процессе"),
    ("completed", "Завершена"),
]


class Task(models.Model):
    """Задача."""

    name = models.CharField("Название", max_length=256)
    description = models.TextField("Описание", null=True, blank=True)
    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default="queued"
    )
    time_created = models.DateTimeField("Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["time_created"]

    def __str__(self):
        return self.name


class TaskDocument(Document):
    name = Text()
    description = Text()
    status = Text()
    time_created = Date()

    class Index:
        name = "tasks"

    @classmethod
    def init_connection(cls):
        connections.create_connection(
            alias="default",
            hosts=[settings.ELASTICSEARCH_DSL["default"]["hosts"]],
        )

    @classmethod
    def create_index(cls):
        cls.init_connection()
        if not cls._index.exists():
            cls.init()

    def save(self, **kwargs):
        self.init_connection()
        return super().save(**kwargs)

    def delete(self, **kwargs):
        self.init_connection()
        return super().delete(**kwargs)
