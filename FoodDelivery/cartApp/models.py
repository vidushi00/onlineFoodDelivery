from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint

from menuApp.models import Menu
from restaurantListingApp.models import Restaurants

STATUS_CHOICES = (
    ('order_confirmed', 'order_confirmed'),
    ('in_cart', 'in_cart'),
)
# Create your models here.

class UsersCart(models.Model):
    food_id = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurants, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_cart')
    UniqueConstraint(fields=['user_id', 'restaurant_id'], name='id')

