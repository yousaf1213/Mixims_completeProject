from django.shortcuts import render

from rest_framework import permissions
from rest_framework.views import APIView
from .models import Product
from rest_framework.decorators import api_view
from django.views import View
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import generics


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


class GenericViews(generics.ListCreateAPIView, generics.CreateAPIView, generics.DestroyAPIView,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'Product_name'
