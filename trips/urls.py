from django.urls import path


from .views import trips

app_name = "trips"

urlpatterns = [
    path('trips/', trips, name="trips"),

]
