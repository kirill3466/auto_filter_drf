from django.urls import path

from .views import (
    VehicleDestroyAPIView,
    VehicleListCreate,
    VehicleRetrieveAPIView,
    VehicleUpdateAPIView,
)

urlpatterns = [
    path(
        'cars/',
        VehicleListCreate.as_view(),
        name='vehicle-list-create'
    ),
    path(
        'cars/<int:pk>/',
        VehicleRetrieveAPIView.as_view(),
        name='vehicle-retrieve'
    ),
    path(
        'cars/<int:pk>/update/',
        VehicleUpdateAPIView.as_view(),
        name='vehicle-update'
    ),
    path(
        'cars/<int:pk>/delete/',
        VehicleDestroyAPIView.as_view(),
        name='vehicle-delete'
    ),
]
