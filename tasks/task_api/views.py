from elasticsearch import NotFoundError
from elasticsearch_dsl import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from task_api.models import Task, TaskDocument
from task_api.serializers import TaskSerializer
from task_api.tasks import process_task


class TaskViewSet(viewsets.ModelViewSet):
    """Представление для задач."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        TaskDocument.init_connection()
        TaskDocument.create_index()
        TaskDocument(**serializer.data).save()
        process_task.delay(task.id)
        return task

    def perform_update(self, serializer):
        task = serializer.save()
        TaskDocument.init_connection()
        TaskDocument.create_index()
        TaskDocument(**serializer.data).save()
        return task

    def perform_destroy(self, instance):
        try:
            TaskDocument.init_connection()
            TaskDocument.create_index()
            TaskDocument.get(id=instance.id).delete()
        except NotFoundError:
            pass
        instance.delete()

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        query = request.query_params.get("q", None)
        if not query:
            return Response(
                {"error": "No query parameter provided"}, status=400
            )

        TaskDocument.init_connection()
        q = Q(
            "multi_match",
            query=query,
            fields=["name", "description", "status"],
        )
        search = TaskDocument.search().query(q)
        response = search.execute()
        results = [hit.to_dict() for hit in response]
        return Response(results)
