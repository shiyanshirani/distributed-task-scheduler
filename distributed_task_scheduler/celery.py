import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "distributed_task_scheduler.settings")

app = Celery(
    "distributed_task_scheduler",
    broker="amqp://{}:{}@{}:{}/{}".format(
        os.environ["RMQ_USERNAME"],
        os.environ["RMQ_PASSWORD"],
        os.environ["RMQ_HOST"],
        os.environ["RMQ_PORT"],
        os.environ["RMQ_V_HOST"],
    ),
)
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_default_queue = "default"
app.conf.task_default_exchange_type = "direct"
app.conf.task_default_routing_key = "default"

# Task Queues
# app.conf.task_queues = (
#     Queue(
#         "sync",
#         Exchange("digital-catalog", type="direct"),
#         routing_key="sync.queue",
#     ),
#     Queue(
#         "mail",
#         Exchange("digital-catalog", type="direct"),
#         routing_key="mail.queue",
#     ),
# )

# # # Task Routes
# app.conf.task_routes = {
#     "email_task.tasks.share_product": {
#         "queue": "mail",
#     },
#     "email_task.tasks.share_feedback": {
#         "queue": "mail",
#     },
#     "core.tasks.import_categories.populate_categories": {
#         "queue": "sync",
#     },
#     "core.tasks.import_to_typesense.typesense_ingress": {
#         "queue": "sync",
#     },
#     "core.tasks.import_to_typesense.delete_skus": {
#         "queue": "sync",
#     },
# }

app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True

# celery -A distributed_task_scheduler worker --loglevel=INFO -Q sync -n "sync-worker"
