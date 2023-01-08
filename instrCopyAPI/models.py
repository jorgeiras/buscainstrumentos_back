from django.db import models

# Create your models here.


class Instrument(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=1000)
    WebSite = models.CharField(max_length=100)

