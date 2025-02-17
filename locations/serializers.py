from rest_framework import serializers
from .models import Location, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'lastname', 'username', 'type']

class LocationSerializer(serializers.ModelSerializer):

    # user = UserSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'created_at', 'status', 'buckets', 'user']

    # Optionally, allow setting the user when creating a location
    # def create(self, validated_data):
    #     request_user = self.context['request'].user
    #     location = Location.objects.create(user=request_user, **validated_data)
    #     return location