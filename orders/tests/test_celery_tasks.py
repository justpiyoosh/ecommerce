from django.test import TestCase
from orders.models import Order
from orders.tasks import process_order

class CeleryTaskTest(TestCase):
    def test_process_order_task(self):
        """Test that Celery task processes an order"""

        order = Order.objects.create(
            order_id=670111,
            user_id=1,
            item_ids=[342,2342,42,42],
            total_amount=100.0,
            status="Pending"
        )

        process_order(order.order_id)

        order.refresh_from_db()
        self.assertEqual(order.status, "Completed")
