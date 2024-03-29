from django.db import models

# Create your models here.


class Instrument(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    link = models.CharField(max_length=1000, unique=True)
    website = models.CharField(max_length=500)
    image = models.CharField(max_length=1000, null=True, default=None)
    location = models.CharField(max_length=500, null=True, default=None)
    category = models.CharField(max_length=200, null=True, default=None)
    expiration = models.DateField(null=True, default=None)
    publish = models.DateField(null=True, default=None)

