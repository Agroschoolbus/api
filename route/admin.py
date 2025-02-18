from django.contrib import admin

# Register your models here.
from .models import Route

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)