from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'year_of_manufacture',
        'fuel_type',
        'transmission',
        'mileage',
        'price',
    )
