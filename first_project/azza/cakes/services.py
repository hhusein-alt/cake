from django.conf import settings
from django.core.mail import send_mail

from .models import Cake


class CakeNotificationService:
    """
    This services handles all kind of notifications
    related to the Cake model.
    """
    @staticmethod
    def send_cake_creation_notification(cake: Cake):
        cake_id = cake.pk

        subject = "Cake created!"
        message = f"Hello, congratulations! Your cake with ID {cake_id} is created!\n\
                    Here is the link: http://127.0.0.1:8000/cakes/{cake_id}/"
        from_email = settings.EMAIL_HOST_USER
        recipients = [
                "thomasdevv77@gmail.com", 
                "ruhinzeynalov6@gmail.com",
                "mammadaliyevmammadali@gmail.com"
            ]

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipients,
                fail_silently=False
            )
        except Exception as err:
            print("Error while sending mail...")