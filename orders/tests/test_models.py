from django.test import TestCase
from orders.models import Order

class OrderModelTest(TestCase):

    def test_create_order(self):
        """Test order model can store and retrieve data correctly"""
        order = Order.objects.create(
            user_id=1,
            item_ids=[1, 2, 3],
            total_amount=200.00,
            status="Pending"
        )
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.total_amount, 200.00)
