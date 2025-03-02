from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from .tasks import process_order
from orders.services import get_total_orders, get_avg_processing_time, get_order_status_counts

@api_view(["POST"])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        process_order.delay(order.order_id)
        return Response({"message": "Order received", "order_id": order.order_id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def order_status(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        return Response({"order_id": order.order_id, "status": order.status})
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def order_metrics(request):
    """Returns order metrics including total orders, avg processing time, and status counts."""
    return Response({
        "total_orders": get_total_orders(),
        "avg_processing_time": get_avg_processing_time(),
        "order_status_counts": get_order_status_counts()
    })
