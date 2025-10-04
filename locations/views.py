from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Location, User
from .serializers import LocationSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

import logging

logger = logging.getLogger(__name__)

class LocationCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = LocationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UserDetailView(APIView):
#     def get(self, request, id):
#         user = get_object_or_404(User, id=id)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class LocationUpdateView(APIView):
    def patch(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location, data=request.data, partial=True)
        # serializer = LocationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.error(f"Invalid data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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