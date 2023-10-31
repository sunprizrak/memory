from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from datetime import datetime
from django.utils import timezone


@shared_task
def send_email_task(*args, **kwargs):
    now = datetime.now().astimezone(timezone.get_current_timezone())
    send_date = kwargs.get('send_date')
    if now >= send_date:
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = kwargs.get('email')
        message = kwargs.get('text')
        name = kwargs.get('name', 'Unknown')
        email = EmailMessage(
            subject=f'Записка от {name}',
            body=message,
            from_email=from_email,
            to=[to_email],
        )

        email.send(fail_silently=False)