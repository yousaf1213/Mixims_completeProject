from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=300, null=True, blank=True)
    password = models.IntegerField()
    exdata = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    Product_name = models.CharField(max_length=30)
    Product_desc = models.CharField(max_length=300, null=True, blank=True)
    Price = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='set_user')

    def __str__(self):
        return self.Product_name


class Message(models.Model):
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.message