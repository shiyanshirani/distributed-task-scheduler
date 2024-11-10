from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Task
from core.serializer import TaskSerializer


class TaskView(APIView):
    """API View to get tasks"""

    def get(self, request):
        task_id = request.query_params.get("id")
        if task_id:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            response = serializer.data
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            response = serializer.data

        return Response(response, status.HTTP_200_OK)

    def post(self, request):
        task = Task.objects.create()
        serializer = TaskSerializer(task)
        response = serializer.data
        return Response(response, status.HTTP_201_CREATED)
