from celery import shared_task
from django.utils.timezone import now
from .models import Order

@shared_task
def process_order(order_id):
    order = Order.objects.get(order_id=order_id)
    order.status = "Processing"
    order.save()

    order.status = "Completed"
    order.processed_at = now()
    order.save()

    return f"Order {order_id} processed"
