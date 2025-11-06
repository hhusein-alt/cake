from django.db import models
from django.contrib.auth.models import User

# ForeignKey
class Order(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    products = models.CharField(max_length=128)
    quantity = models.IntegerField(null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order No.{self.pk}"
    
    # one-to-many relationship