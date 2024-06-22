from celery import shared_task
from apps.utils import send_email


@shared_task()
def task_send_email(subject, msg, recipient_list):
    send_email(subject, msg, recipient_list)
    return {
        'subject': 'New product message for recipients',
        'emails': recipient_list,
        'success': True
    }


@shared_task()
def task_contact_with(subject, message, recipient):
    send_email(subject, message, recipient)
    return {
        'subject': 'Contact message for recipient',
        'email': recipient,
        'success': True
    }
