from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Status, Task
from core.tasks import run_task


@receiver(post_save, sender=Task)
def initiate(sender, instance, *args, **kwargs):
    if instance.status == Status.Scheduled:
        run_task.delay(instance.id)
