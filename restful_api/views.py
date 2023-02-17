import time
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Product, User
from rest_framework.decorators import api_view
from django.views import View
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import ProductSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import generics
import threading as thread
from faker import Faker
fake=Faker()
import requests
from django.conf import settings
from django.core.mail import send_mail


class SnippetList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all().values()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.method == 'POST':
            data = request.data
            a = Product.objects.create(Product_name=data.get("Product_name"), Product_desc=data.get("Product_desc"),
                                       Price=data.get("Price"))
            a.save()
            return Response("saved Successfully")

    def delete(self, request, format=None):
        if request.method == 'DELETE':
            data = request.data
            a = Product.objects.filter(Product_name=data.get("Product_name")).delete()
            return Response("deleted Successfully")

    def put(self, request, format=None):
        if request.method == 'PUT':
            data = request.data
            a = Product.objects.get(Product_name=data.get("Product_name"))
            a.Product_name = data.get("new_Product_name")
            a.Product_desc = data.get("Product_desc")
            a.Price = data.get("Price")
            a.save()
            return Response("Updated Successfully")


# @api_view(['GET', 'POST'])
# def baseserialize(request):
#     a = Product.objects.filter(Product_name="iphone 12 pro max")
#     serializer = PostProductSerializer(a, many=True)
#     return Response(serializer.data)


class GenericViews(generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class GetorInsertProduct(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetorInsertUser(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCrud(generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

def bck(total):
    data=User.objects.values_list('pk',flat=True)
    time.sleep(2)
    for i in range(total):
        print("Product ",i,"Created")
        Product.objects.create(
            Product_name=fake.name(),
            Product_desc = fake.text(),
            Price=fake.random_int(3000, 10000),
            user=User.objects.order_by('id').first()
        )


def AsyncInsertUsingThread(request):
    count = 5
    t = thread.Thread(target=bck, args=[count])
    t.start()
    return HttpResponse("Work Started")



def scraphelper():
    from bs4 import BeautifulSoup
    from django.core.mail import send_mail
    r = requests.get('https://www.pakwheels.com/used-cars/search/-/')
    img = BeautifulSoup(r.content, 'html.parser')
    images_list = []
    images = img.select('img')
    for image in images:
        src = image.get('data-original')
        images_list.append({"src": src})
    for image in images_list:
        print(image)

    subject = 'welcome to the app'
    message = f'hiii \n The list is as follow \n ' + f"\n".join([str(src) for src in images_list])
    email_from = 'yz255849@gmail.com'
    recipient_list = ['f180111@nu.edu.pk', ]
    send_mail(subject, message, email_from, recipient_list)


def WebScrapp(request):
    t = thread.Thread(target=scraphelper)
    t.start()
    return HttpResponse("Work Started")