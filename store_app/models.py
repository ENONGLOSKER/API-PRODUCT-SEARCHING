from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Store(models.Model):
    name_store = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='stores')

    def __str__(self) -> str:
        return self.name_store
