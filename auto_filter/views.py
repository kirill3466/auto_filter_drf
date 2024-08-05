from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Vehicle
from .pagination import VehiclePagination
from .serializers import VehicleSerializer


class VehicleListCreate(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = VehiclePagination

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        filters = {
            'brand__icontains': params.get('brand'),
            'model__icontains': params.get('model'),
            'year_of_manufacture': params.get('year_of_manufacture'),
            'fuel_type': params.get('fuel_type'),
            'transmission': params.get('transmission'),
            'mileage__gte': params.get('mileage_min'),
            'mileage__lte': params.get('mileage_max'),
            'price__gte': params.get('price_min'),
            'price__lte': params.get('price_max')
        }
        queryset = self.apply_filters(queryset, filters)
        return queryset

    def apply_filters(self, queryset, filters):
        for key, value in filters.items():
            if value:
                queryset = queryset.filter(**{key: value})
        return queryset


class VehicleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class VehicleUpdateAPIView(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class VehicleDestroyAPIView(generics.DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
