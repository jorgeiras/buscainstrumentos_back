from django.db import models

# Create your models here.


class Instrument(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=1000, unique=True)
    website = models.CharField(max_length=500, default="null")
    image = models.CharField(max_length=1000, default="null")
    location = models.CharField(max_length=500, default="null")
    category = models.CharField(max_length=200, default="null")
    expiration = models.DateField()
    publish = models.DateField()

