from django.db import models
from accounts.models import Generaluser

class Advertisement(models.Model):
    host = models.ForeignKey(Generaluser, related_name='advertise', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    map_location = models.TextField()
    availability = models.BooleanField(default=True)
    safety = models.TextField()
    weather = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    speciality = models.TextField()
    city_size = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail_picture = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_6_months = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_1_year = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent_individual = models.DecimalField(max_digits=10, decimal_places=2)
    groceries_individual = models.DecimalField(max_digits=10, decimal_places=2)
    others_individual = models.DecimalField(max_digits=10, decimal_places=2)
    total_individual = models.DecimalField(max_digits=10, decimal_places=2)
    rent_family = models.DecimalField(max_digits=10, decimal_places=2)
    groceries_family = models.DecimalField(max_digits=10, decimal_places=2)
    others_family = models.DecimalField(max_digits=10, decimal_places=2)
    total_family = models.DecimalField(max_digits=10, decimal_places=2)
    pictures = models.JSONField(default=list) 

    review_count = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    comments = models.JSONField(default=list)

    def __str__(self):
        return self.title
