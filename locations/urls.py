# locations/urls.py
from django.urls import path
from .views import LocationCreateView, LocationListView, LocationUpdateView, UserCreateView, UserDetailView

urlpatterns = [
    path('locations/<int:pk>/update/', LocationUpdateView.as_view(), name='update_location'),
    path('users/<str:pk>/', UserDetailView.as_view(), name='user_details'),
    path('add-location/', LocationCreateView.as_view(), name='add_location'),
    path('add-user/', UserCreateView.as_view(), name='add_user'),
    path('locations/', LocationListView.as_view(), name='location-list'),
]