from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Cake


class CakeNotificationService:
    """
    This service handles all kinds of notifications
    related to the Cake model.
    """
    @staticmethod
    def send_cake_creation_mail(cake_id: Cake):
        subject = "🎂 New Cake Created!"
        from_email = settings.EMAIL_HOST_USER
        recipients = [
            "thomasdevv77@gmail.com",
            "ruhinzeynalov6@gmail.com",
            "mammadaliyevmammadali@gmail.com"
        ]

        # Context for the template
        context = {
            "cake": Cake.objects.filter(pk=cake_id).first(),
            "cake_link": f"http://127.0.0.1:8000/cakes/{cake_id}/"
        }

        # Plain-text fallback
        text_content = (
            f"Hello!\n"
            f"Your cake with ID {cake_id} has been created successfully.\n"
            f"View it here: {context['cake_link']}"
        )

        # Render HTML version
        html_content = render_to_string("/Users/mammadaliyevmammadali/Desktop/first_project/azza/cakes/templates/emails/cake_created.html", context)

        try:
            msg = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=from_email,
                to=recipients
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except Exception as err:
            print("Error while sending mail:", err)