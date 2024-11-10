from django.contrib import admin

from core.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "failed_reason",
        "created_at",
        "updated_at",
    )


admin.site.register(Task, TaskAdmin)
