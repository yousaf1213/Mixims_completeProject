from django.db import models
import uuid



class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=300, null=True, blank=True)
    password = models.IntegerField()
    def __str__(self):
        return self.name

class Product(models.Model):
    Product_name = models.CharField(max_length=30)
    Product_desc = models.CharField(max_length=300, null=True, blank=True)
    Price = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='set_user')

    def __str__(self):
        return self.Product_name
