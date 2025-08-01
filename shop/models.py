from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id}- {self.name} costs ${self.price}'