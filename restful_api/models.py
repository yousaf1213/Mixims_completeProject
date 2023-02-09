from django.db import models
import uuid


class Product(models.Model):
    Product_name = models.CharField(max_length=30)
    Product_desc = models.CharField(max_length=300, null=True, blank=True)
    Price = models.IntegerField()
    Id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)

    def __str__(self):
        return self.Product_name
