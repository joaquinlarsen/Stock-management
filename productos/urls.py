from django.urls import path
from .views import (
    deleteOrder,
    productos,
    createOrder,
    updateOrder,
    deleteOrder,
)

urlpatterns = [
    path("", productos, name="productos"),
    path("create_order/", createOrder, name="create_order"),
    path("update_order/<str:pk>/", updateOrder, name="update_order"),
    path("delete_order/<str:pk>/", deleteOrder, name="delete_order"),
]
