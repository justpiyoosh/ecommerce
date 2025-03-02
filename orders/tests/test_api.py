from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from orders.models import Order

class OrderAPITest(APITestCase):

    def setUp(self):
        self.create_order_url = reverse("create_order")
        self.metrics_url = reverse("order_metrics")

    def test_create_order(self):
        """Test API can create an order"""
        payload = {
            "user_id": 1,
            "order_id": 45308,
            "item_ids": [1, 2, 3],
            "total_amount": 150.00
        }
        response = self.client.post(self.create_order_url, data=payload, format="json")
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_get_order_metrics(self):
        """Test order metrics endpoint"""
        response = self.client.get(self.metrics_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
