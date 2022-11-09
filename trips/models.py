from django.db import models

# Create your models here.
class TripDetails(models.Model):
    driver_id = models.IntegerField(max_length=30)
    vehicle_id = models.IntegerField(max_length=30)
    customer_id = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    cargo_tonnage = models.DecimalField(max_digits = 10, decimal_places = 2)
    # cargo_type = models.DecimalField(max_)





    last_name = models.CharField(max_length=30)