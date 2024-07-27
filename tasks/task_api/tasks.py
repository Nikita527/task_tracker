import time

from celery import shared_task

from task_api.models import Task


@shared_task
def process_task(task_id):
    task = Task.objects.get(id=task_id)
    task.status = "in_progress"
    task.save()
    time.sleep(10)
    task.status = "completed"
    task.save()
