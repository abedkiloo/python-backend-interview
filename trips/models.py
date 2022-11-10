from django.db import models
from django.conf import settings

class TripDetails(models.Model):

    PICK_UP_POINT = 'pick_up_point'
    DROP_OF_POINT = 'drop_off_point'

    PICK_UP_CONF = (
        (PICK_UP_POINT, 'pick_up_point'),
        (DROP_OF_POINT, 'drop_off_point'),
    )

    driver_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    customer_id = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    cargo_tonnage = models.DecimalField(max_digits = 10, decimal_places = 2)
    cargo_type = models.CharField(max_length=255, choices=PICK_UP_CONF, default=PICK_UP_POINT)
    done_by_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






