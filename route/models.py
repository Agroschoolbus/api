from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100, unique=True)
    data = models.TextField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    mill_lat = models.DecimalField(max_digits=9, decimal_places=6)
    mill_lon = models.DecimalField(max_digits=9, decimal_places=6)

    center_lat = models.DecimalField(max_digits=9, decimal_places=6)
    center_lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name