from rest_framework import serializers
from .models import Customer, Product, Supplier, Category, Employee, Order
from django.contrib.auth.models import User


class SupplierSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Supplier
        fields = ['id', 'companyname', 'contactname', 'address', 'city', 'postalcode', 'country', 'phone', 'owner']

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['id', 'productname', 'packagesize', 'unitprice', 'unitsinstock', 'supplier', 'category', 'discontinued', 'owner']

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = ['id', 'categoryname', 'description', 'owner']

class UserSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all())
    product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    customer = serializers.PrimaryKeyRelatedField(many=True, queryset=Customer.objects.all())
    employee = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'supplier', 'product', 'category', 'customer', 'employee']

class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Customer
        fields = ['id', 'companyname', 'contactname', 'address', 'city', 'postalcode', 'country', 'phone', 'owner']

class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Employee
        fields = ['id', 'firstname', 'lastname', 'email', 'address', 'city', 'postalcode', 'country', 'phone', 'photo', 'birthdate', 'hireddate', 'owner']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'employee', 'orderdate', 'shippeddate', 'shipname', 'shipaddress', 'shipcity', 'shippostalcode', 'shipcountry']




