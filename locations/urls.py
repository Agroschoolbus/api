# locations/urls.py
from django.urls import path
from .views import LocationCreateView, LocationListView

urlpatterns = [
    path('add-location/', LocationCreateView.as_view(), name='add_location'),
    path('locations/', LocationListView.as_view(), name='location-list'),
]