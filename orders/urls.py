from django.urls import path
from .views import create_order, order_status, order_metrics

urlpatterns = [
    path("metrics/", order_metrics, name="order_metrics"),
    path("", create_order, name="create_order"),
    path("<str:order_id>/", order_status, name="order_status"),
]
