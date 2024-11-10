from django.urls import path

from core.views import TaskView

urlpatterns = [path("task", TaskView.as_view(), name="Task API")]
