from django.db import models


class FuelType(models.TextChoices):
    GASOLINE = "бензин"
    DIESEL = "дизель"
    ELECTRIC = "электричество"
    HYBRID = "гибрид"


class TransmissionType(models.TextChoices):
    MANUAL = "мануальная"
    AUTOMATIC = "автоматическая"
    VARIATOR = "вариатор"
    ROBOT = "робот"


class Vehicle(models.Model):
    brand = models.CharField(
        verbose_name="Марка",
        max_length=100
    )
    model = models.CharField(
        verbose_name="Модель",
        max_length=100
    )
    year_of_manufacture = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска"
    )
    fuel_type = models.CharField(
        verbose_name="Тип топлива",
        max_length=100,
        choices=FuelType.choices,
    )
    transmission = models.CharField(
        verbose_name="Коробка передач",
        max_length=100,
        choices=TransmissionType.choices
    )
    mileage = models.PositiveSmallIntegerField(
        verbose_name="Пробег"
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
