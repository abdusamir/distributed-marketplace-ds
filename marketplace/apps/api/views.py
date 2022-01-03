from django.shortcuts import render
from rest_framework import generics
from apps.product.models import Product
from apps.order.models import Order
from apps.vendor.models import Vendor
from .serializers import ProductSerializer, OrderSerializer,VendorSerializer
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer

class OrderList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Order.objects.all()
    serializer_class = OrderSerializer
    
class VendorList(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class = VendorSerializer
    
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class = VendorSerializer