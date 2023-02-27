from django.db.models.signals import pre_delete, post_delete,post_save,pre_save
from .models import Product,User
from django.dispatch import receiver
import requests
from rest_framework.response import Response
from . import views

@receiver(post_save,sender=User)
def post_profile(sender,instance,**kwargs):
    data1=instance
    print(data1)
    data(data1)
    return Response("saved Successfully")



def data(data1):
    url = 'https://dog.ceo/api/breeds/image/random'
    api_call = requests.get(url, headers={})
    data = api_call.json().get('message')
    User.objects.filter(name=data1).update(exdata=data)
    print("Doneeee")

@receiver(pre_delete, sender=Product)
def pre_delete_profile(sender, **kwargs):
    print("You are about to delete something!")

@receiver(post_delete, sender=Product)
def delete_profile(sender, **kwargs):
    print("You have just deleted a Product!!!")