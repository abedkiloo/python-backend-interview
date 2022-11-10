from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import TripDetails

from .serializers import TripSerializer



@api_view(['GET','POST', 'PUT', ])
@permission_classes((permissions.AllowAny,))
def trips(request, version):
    try:
        trip_details  = TripDetails.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TripSerializer(trip_details, context={"request": request})
        return Response({
            "status": True,
            "data": serializer.data})


    if request.method == "POST":
        request_data = dict(request.data)
        request_data["done_by_user"] = request.user.id
        serializer = TripSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

