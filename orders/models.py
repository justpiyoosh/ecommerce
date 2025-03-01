from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Completed", "Completed"),
    ]

    user_id = models.IntegerField()
    order_id = models.CharField(max_length=255, unique=True)
    item_ids = models.JSONField()
    total_amount = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
