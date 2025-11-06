from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cake
from .services import CakeNotificationService
from .tasks import send_mail_for_cake_creation


@receiver(post_save, sender=Cake)
def cake_created_signal(sender, instance, created, **kwargs):
    if created:
        send_mail_for_cake_creation.delay(instance.pk)
