from django.contrib.auth.models import User
from django.db import models

# Create your models here.
STATUS_CHOICES = (('delivered', 'delivered'), ('in_transit', 'in_transit'))
PAYMENT_CHOICES = (('cash_on_delivery', 'cash_on_delivery'), ('UPI', 'UPI'))

class DeliveryDetail(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    no_of_items = models.IntegerField(null=False, blank=False)
    delivery_agent = models.CharField(max_length=100, null=True, blank=True)
    delivery_location = models.CharField(max_length=1000, null=False, blank=False)
    total_amount = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='payment_pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
