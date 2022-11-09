from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import TripDetails


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TripDetails
        fields = [

              "driver_id","vehicle_id", "customer_id","address","cargo_tonnage",'cargo_type' ,'done_by_user_id'
        ]
