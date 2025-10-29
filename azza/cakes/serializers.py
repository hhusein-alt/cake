from rest_framework import serializers
from .models import Cake


class CakePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = [
            "id",
            "name",
            "price"
        ]


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = [
            "id",
            "name",
            "price",
            "size",
            "stock",
            "ingredients",
            "created_at"
        ]
