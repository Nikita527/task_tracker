import os

from dotenv import load_dotenv

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from task_api.models import Task, TaskDocument  # noqa

load_dotenv()

TaskDocument.init_connection()
TaskDocument.init()

tasks = [
    {"name": "Задача 1", "description": "Описание задачи 1"},
    {"name": "Задача 2", "description": "Описание задачи 2"},
    {"name": "Задача 3", "description": "Описание задачи 3"},
]

for task_data in tasks:
    task = Task.objects.create(**task_data)
    task_doc = TaskDocument(
        meta={"id": task.id},
        name=task.name,
        description=task.description,
        status=task.status,
        time_created=task.time_created,
    )
    task_doc.save()
    print(f"Задача создана: {task.name}")
