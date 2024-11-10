from uuid import uuid4

from django.db import models


class Status(models.TextChoices):
    Scheduled = "Scheduled", "SCHEDULED"
    In_Progress = "In Progress", "IN_PROGRESS"
    Completed = "Completed", "COMPELTED"
    Failed = "Failed", "FAILED"


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.Scheduled,
    )
    failed_reason = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def mark_as_success(self):
        self.status = Status.Completed
        self.save()

    def mark_as_in_progress(self):
        self.status = Status.In_Progress
        self.save()

    def mark_as_failed(self):
        self.status = Status.Failed
        self.save()

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"
