from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    size = models.IntegerField()
    ingredients = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ${self.price}"
