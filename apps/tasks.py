from celery import shared_task
from apps.utils import send_email


@shared_task()
def task_send_email(subject, msg, recipient_list):
    send_email(subject, msg, recipient_list)
    return {
        'emails': recipient_list,
        'success': True
    }
