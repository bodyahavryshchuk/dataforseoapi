from rest_framework import generics, views
from rest_framework.response import Response

from src.tasks import services, serializers
from src.tasks import models


class TaskCreateView(views.APIView):
    """ Create task view """
    serializer_class = serializers.TaskCreateSerializer

    def post(self, request):
        return services.task_post(self, request)


class TaskListView(generics.ListAPIView):
    """ Get task list view """
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class TaskDataListView(generics.ListAPIView):
    """ Get task data list view """
    serializer_class = serializers.TaskDataSerializer
    queryset = models.TaskData.objects.all()


class TaskResultListView(generics.ListAPIView):
    """ Get result list for task view """
    serializer_class = serializers.TaskResultSerializer

    def get_queryset(self):
        return services.task_get(self)
