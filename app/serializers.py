from rest_framework import serializers
from .models import Product, Supplier, User


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'companyname', 'contactname', 'address', 'phone', 'email', 'country']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productname', 'packagesize', 'unitprice', 'unitsinstock', 'supplier']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'username', 'password', 'accesslevelid']

