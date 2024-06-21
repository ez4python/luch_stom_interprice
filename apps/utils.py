from django.core.mail import send_mail
from django.http import JsonResponse

from root import settings


# email sender service
def send_email(subject, message, to_email: list):
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, to_email, False)
    return JsonResponse({'status': 'success'})
