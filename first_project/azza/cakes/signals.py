from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cake
from .services import CakeNotificationService


@receiver(post_save, sender=Cake)
def cake_created_signal(sender, instance, created, **kwargs):
    if created:
        # CakeNotificationService.send_cake_creation_notification(instance)
        pass