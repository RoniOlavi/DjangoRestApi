from django.contrib import admin

from .models import Supplier, Product, Category, Employee, Customer, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): # Sekä rekisteröidä kyseisellä metodilla
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin): # Sekä rekisteröidä kyseisellä metodilla
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): # Sekä rekisteröidä kyseisellä metodilla
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin): # Sekä rekisteröidä kyseisellä metodilla
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): # Sekä rekisteröidä kyseisellä metodilla
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): # Sekä rekisteröidä kyseisellä metodilla
    pass
