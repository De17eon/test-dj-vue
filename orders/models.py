from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class SalesOrder(models.Model):
    bubun = models.CharField(max_length=150, null=True)
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)


