from django.db import models

# Create your models here.

class Restaurants(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=158, null=False, blank=False)
    location = models.CharField(max_length=500, null=False, blank=False)
    rating = models.IntegerField(max_length=10, null=True, blank=True)

