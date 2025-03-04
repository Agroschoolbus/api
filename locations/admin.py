from django.contrib import admin

# Register your models here.
from .models import Location, User

# admin.site.register(Location)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'username', 'type')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'bags', 'buckets', 'user', 'created_at')