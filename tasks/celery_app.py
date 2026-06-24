from celery import Celery
celery_app = Celery(
    "space_r",
    broker="redis://localhost:6379/0"
)