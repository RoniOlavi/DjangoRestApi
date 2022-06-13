from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Suppliers
    path('api/suppliers', views.SuppliersList.as_view()),
    path('api/suppliers/<int:pk>/', views.SupplierDetail.as_view()),
    # Products
    path('api/products', views.ProductList.as_view()),
    path('api/products/<int:pk>/', views.ProductDetail.as_view()),
    # Users
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),
    # Categories
    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>/', views.CategoryDetail.as_view()),
    # Customers
    path('api/customers/', views.CustomerList.as_view()),
    path('api/customers/<int:pk>/', views.CustomerDetail.as_view()),
    # Employees
    path('api/employees/', views.EmployeeList.as_view()),
    path('api/employees/<int:pk>/', views.EmployeeDetail.as_view()),
    # Orders
    path('api/orders/', views.OrderList.as_view()),
    path('api/orders/<int:pk>/', views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)