import time
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Product, User, Message
from rest_framework.decorators import api_view
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .serializers import ProductSerializer, UserSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework import generics
import threading as thread
from faker import Faker

fake = Faker()
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


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
    data = User.objects.values_list('pk', flat=True)
    time.sleep(2)
    for i in range(total):
        print("Product ", i, "Created")
        Product.objects.create(
            Product_name=fake.name(),
            Product_desc=fake.text(),
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


def dictComp(request):
    dictionary = dict()
    for k1 in range(11, 16):
        dictionary[k1] = dict()
        for k2 in range(1, 6):
            dictionary[k1][k2] = k1 * k2
    print(dictionary)
    return HttpResponse("printed dictionary")


def listComp(request):
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = [x if x != "banana" else "orange" for x in fruits]

    print(newlist)
    return HttpResponse("printed List")


def postgresSearch(request):
    vector = SearchVector('Product_name', 'Product_desc')
    query = SearchQuery('pick')
    products = Product.objects.annotate(search=vector).filter(search=query).values()
    return HttpResponse(products.get('Product_desc') for products in products)


import stripe

from django.views.decorators.csrf import csrf_exempt

YOUR_DOMAIN = 'http://127.0.0.1:8000'


@api_view(['POST'])
def stripePayment(self, format=None):
    stripe.api_key = 'sk_test_51MBfbdDjBgI52bwWj73IhtqddWHqR5Bv2rxXRtZWm1uiglA6CD3mrq1MLYcQfckir7BXRrqh9HDFtGKzfBl7ECiK00weAtshHv'

    # stripe.PaymentMethod.create(
    #     type="card",
    #     card={
    #         "number": self.data.get('card_no'),
    #         "exp_month": self.data.get('exp_month'),
    #         "exp_year": self.data.get('exp_year'),
    #         "cvc": self.data.get('cvc'),
    #     },
    #
    #     metadata={'order_id': self.data.get('order_id'), 'amount':self.data.get('amount')}
    # ),

    stripe.Charge.create(

        amount=self.data.get('amount'),
        currency="usd",
        # type="card",
        card={
            "number": self.data.get('card_no'),
            "exp_month": self.data.get('exp_month'),
            "exp_year": self.data.get('exp_year'),
            "cvc": self.data.get('cvc'),
        },
        metadata={'order_id': self.data.get('order_id')}
    )

    return HttpResponse("Payment Made Successfully")


@api_view(['POST'])
def stripeRefund(self, format=None):
    stripe.api_key = "sk_test_51MBfbdDjBgI52bwWj73IhtqddWHqR5Bv2rxXRtZWm1uiglA6CD3mrq1MLYcQfckir7BXRrqh9HDFtGKzfBl7ECiK00weAtshHv"

    stripe.Refund.create(
        charge=self.data.get("charge"),
    )
    return HttpResponse("Refunded Successfully")


@api_view(['POST'])
def login(request):
    from django.contrib.auth import login, authenticate  # add this
    if request.method == "POST":
        User = authenticate(name=request.data.get('name'), password=request.data.get('password'))
        if User is not None:
            form = login(request, User)
            return HttpResponse(f"You are now logged in as .")
        else:
            return HttpResponse("Invalid username or password.")


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


@api_view(['POST'])
def messageInsert(request):
    if request.method == 'POST':
        a = Message.objects.create(message=request.data.get('message'))
        a.save()

    return HttpResponse("Data inserted Successfully")

@api_view(['GET'])
def getMessages(request):
    message = Message.objects.all().values()
    data = []
    data.append(f"\n".join([str(message.get('message')) for message in message]))

    return HttpResponse(data)
