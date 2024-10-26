from rest_framework import serializers
from .models import Location, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'lastname', 'username', 'type']

class LocationSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'created_at', 'status', 'user']

    # Optionally, allow setting the user when creating a location
    def create(self, validated_data):
        request_user = self.context['request'].user  # Use the current logged-in user
        location = Location.objects.create(user=request_user, **validated_data)
        return location