from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from django_filters.rest_framework import DjangoFilterBackend

class LocationCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = LocationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user']
    filterset_fields = {
        'user': ['exact'], 
        'created_at': ['exact', 'gte', 'lte'],  # Filters by exact date, start date, or end date
        'status': ['exact'],
    }