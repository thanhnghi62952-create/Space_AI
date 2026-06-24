from tasks.celery_app import celery_app
@celery_app.task
def generate_image_task(state):
    ...