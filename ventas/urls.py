from django.urls import path
from .views import ventas, createVenta

urlpatterns = [
    path("", ventas, name="ventas"),
    path("create_venta/", createVenta, name="create_venta"),
]
