from datetime import timedelta
from django.utils import timezone
from django.db import models


class OTPCode(models.Model):
    email = models.EmailField(max_length=64)
    otp_code = models.CharField(max_length=6)
    expires_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"OTP Code: {self.otp_code} ({self.email})"

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=1)
        return super().save(*args, **kwargs)