# locations/urls.py
from django.urls import path
from .views import RouteDetailAPIView

urlpatterns = [
    path('<int:pk>/', RouteDetailAPIView.as_view(), name='update_route'),
]