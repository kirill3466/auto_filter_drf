from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'brand',
            'model',
            'year_of_manufacture',
            'fuel_type',
            'transmission',
            'mileage',
            'price',
        ]
