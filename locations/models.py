
from django.db import models


class User(models.Model):
    # Primary key (id) is automatically created by Django, no need to declare it explicitly
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    
    USER_TYPES = [
        ('producer', 'Producer'),
        ('consumer', 'Consumer'),
    ]
    type = models.CharField(max_length=10, choices=USER_TYPES, default='producer')

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.username})"


class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    # status = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('selected', 'Selected'), ('collected', 'Collected'), ('delivered', 'Delivered')],
        default='pending'
    )
    buckets = models.IntegerField()
    bags = models.IntegerField()
    mill = models.CharField(
        max_length=20,
        choices=[('mill_1', 'Mill_1'), ('mill_2', 'Mill_2'), ('mill_3', 'Mill_3')],
        default='mill_1'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return f"Location({self.latitude}, {self.longitude}) - User: {self.user.username}"

    # def __str__(self):
    #     return f"Location({self.latitude}, {self.longitude})"