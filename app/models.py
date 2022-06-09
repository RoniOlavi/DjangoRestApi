from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="Yrityksen nimi")
    contactname = models.CharField(max_length = 50, default="Yhteyshenkilö")
    address = models.CharField(max_length = 100, default="Osoite")
    phone = models.CharField(max_length = 20, default="Puhelin")
    email = models.CharField(max_length = 50, default="Sähköposti")
    country = models.CharField(max_length = 50, default="Maa")

    class Meta:
        ordering = ['id']


class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "Tuote nimi")
    packagesize = models.CharField(max_length = 20, default = 1)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        ordering = ['productname']

class User(models.Model):
    firstname = models.CharField(max_length=50, default="Etunimi")
    lastname = models.CharField(max_length=50, default="Sukunimi")
    email = models.CharField(max_length=50, default="Sähköposti")
    username = models.CharField(max_length=50, default="Käyttäjänimi")
    password = models.CharField(max_length=50, default="Salasana")
    accesslevelid = models.IntegerField(default= 2)

    class Meta:
        ordering = ['firstname']