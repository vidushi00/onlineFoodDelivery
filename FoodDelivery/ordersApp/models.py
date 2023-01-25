from django.contrib.auth.models import User
from django.db import models

from menuApp.models import Menu
from restaurantListingApp.models import Restaurants


# Create your models here.

class Orders(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    food_id = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurants, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
