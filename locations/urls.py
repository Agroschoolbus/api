# locations/urls.py
from django.urls import path
from .views import LocationCreateView

urlpatterns = [
    path('add-location/', LocationCreateView.as_view(), name='add_location'),
]