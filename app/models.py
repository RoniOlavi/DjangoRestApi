from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="")
    contactname = models.CharField(max_length = 50, default="")
    address = models.CharField(max_length = 100, default="")
    city = models.CharField(max_length = 50, default="")
    postalcode = models.CharField(max_length = 20, default="")
    country = models.CharField(max_length = 50, default="")
    phone = models.CharField(max_length = 20, default="")
    owner = models.ForeignKey('auth.User', related_name='supplier', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

class Category(models.Model):
    categoryname = models.CharField(max_length = 50, default="")
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "Tuote nimi")
    packagesize = models.CharField(max_length = 20, default = 1)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discontinued = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)

    class Meta:
        ordering = ['productname']

class Customer(models.Model):
    companyname = models.CharField(max_length = 50, default="")
    contactname = models.CharField(max_length = 50, default="")
    address = models.CharField(max_length = 100, default="")
    city = models.CharField(max_length = 50, default="")
    postalcode = models.CharField(max_length = 20, default="")
    country = models.CharField(max_length = 50, default="")
    phone = models.CharField(max_length = 20, default="")
    owner = models.ForeignKey('auth.User', related_name='customer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

class Employee(models.Model):
    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    address = models.CharField(max_length = 100, default="")
    city = models.CharField(max_length = 50, default="")
    postalcode = models.CharField(max_length = 20, default="")
    country = models.CharField(max_length = 50, default="")
    phone = models.CharField(max_length = 20, default="")
    photo = models.ImageField(blank=True)
    birthdate = models.DateTimeField(blank=True)
    hireddate = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='employee', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(auto_now_add=True)
    shippeddate = models.DateTimeField(blank=True)
    shipname = models.CharField(max_length=100, default='')
    shipaddress = models.CharField(max_length = 100, default="")
    shipcity = models.CharField(max_length = 50, default="")
    shippostalcode = models.CharField(max_length = 20, default="")
    shipcountry = models.CharField(max_length = 50, default="")

    class Meta:
        ordering = ['shippeddate']

''' For frontend test
class User(models.Model):
    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    accesslevelid = models.IntegerField(default="")

    class Meta:
        ordering = ['firstname']
'''