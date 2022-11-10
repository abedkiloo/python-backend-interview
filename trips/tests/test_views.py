import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse,reverse_lazy
from ..models import TripDetails
from ..serializers import TripSerializer



client = Client()


class CreateNewTrpDetailTest(TestCase):
    """ Test module for inserting a new trip detail """

    def setUp(self):
        self.valid_payload = {
            "driver_id": "1",
            "vehicle_id": "111",
            "customer_id": "jkkghkgkhg",
            "address": "jkkjgkhghkgh",
            "cargo_tonnage": 100.50  ,
            "cargo_type":"pick_up_point"
        }
        self.invalid_payload = {
            "driver_id": "1",
            "vehicle_id": "111",
            "customer_id": "jkkghkgkhg",
            "address": "jkkjgkhghkgh",
            "cargo_tonnage": 100.50   ,
            "cargo_type":"pick_up_powint"
        }

    def test_create_valid_trip_detail(self):
        response = client.post(
            reverse('trips:trips', kwargs={"version":"v1"}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_trp_detail(self):
        response = client.post(
            reverse('trips:trips', kwargs={"version":"v1"}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)