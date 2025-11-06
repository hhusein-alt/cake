import time

from celery import shared_task
from .services import CakeNotificationService


@shared_task
def send_mail_for_cake_creation(cake_instance_id):
    CakeNotificationService.send_cake_creation_mail(cake_instance_id)
