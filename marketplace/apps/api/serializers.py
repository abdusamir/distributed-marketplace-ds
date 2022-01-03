from apps.product.models import Product
from apps.order.models import Order
from apps.vendor.models import Vendor

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'id',
            'title',
            'category',
            'description',
            'price',
            'vendor',
            'image',
            'slug'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=[
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'paid_amount',
            'vendor'
        ]
        
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=[
            'id',
            'name',
            'created_at'
        ]