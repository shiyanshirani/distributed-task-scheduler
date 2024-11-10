import logging
import random
import typing
from uuid import uuid4

from celery import shared_task

from core.models import Task

logger = logging.getLogger("dts-logger")


@shared_task(bind=True)
def run_task(self, task_id: uuid4, max_retries=3):
    try:
        task = Task.objects.get(id=task_id)
        task.mark_as_in_progress()
        randomly_raise_exception()
        long_sub_task(task)
        task.mark_as_success()
    except Exception as exc:
        if self.request.retries == max_retries:
            task.mark_as_failed()
            task.failed_reason = str(exc)
            task.save()
        else:
            run_task.retry(exc=exc, countdown=5)


def randomly_raise_exception() -> typing.Union[Exception, None]:
    """This function randaomly raises an exception"""
    if random.choice([0, 1]):
        raise Exception()
    return None


def long_sub_task(task: Task) -> int:
    """This is a sub task placeholder function"""
    # Make use of Task object
    sum = 0
    for number in range(1_000_000):
        sum += number
    return sum
