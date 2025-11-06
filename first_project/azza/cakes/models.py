from django.db import models
from django.contrib.auth.models import User


class Cake(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=32, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    size = models.CharField(
        max_length=32, 
        null=True, 
        blank=True,
        choices=SIZE_CHOICES
    )
    # models.JSONField(default=dict)
    ingredients = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ${self.price}"
