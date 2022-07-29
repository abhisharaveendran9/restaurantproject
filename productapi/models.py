from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=120)
    category=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    rating=models.FloatField()


    def __str__(self):
        return self.name
