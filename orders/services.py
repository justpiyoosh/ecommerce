from django.db.models import Avg, F, ExpressionWrapper, fields, Count
from orders.models import Order

def get_total_orders():
    """Returns total number of orders."""
    return Order.objects.count()

def get_avg_processing_time():
    """Returns the average processing time in seconds for completed orders."""
    avg_time = Order.objects.filter(status="Completed").annotate(
        processing_time=ExpressionWrapper(
            F("processed_at") - F("created_at"),
            output_field=fields.DurationField()
        )
    ).aggregate(avg_processing_time=Avg("processing_time"))["avg_processing_time"]

    return avg_time.total_seconds() if avg_time else 0

def get_order_status_counts():
    """Returns a count of orders in each status."""
    return Order.objects.values("status").annotate(count=Count("status"))
