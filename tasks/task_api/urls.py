from rest_framework.routers import DefaultRouter

from django.urls import include, path

from task_api.views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
