from django.db import models

from restaurantListingApp.models import Restaurants


# Create your menu models here.

class Menu(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    restaurant_id = models.ForeignKey(Restaurants, null=False, blank=False, on_delete=models.CASCADE)
    dish = models.CharField(max_length=158, null=False, blank=False)
    rating = models.FloatField(null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)