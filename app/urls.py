from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Suppliers
    path('api/suppliers', views.SuppliersList.as_view()),
    path('api/suppliers/<int:id>/', views.SupplierDetail.as_view()),
    # Products
    path('api/products', views.ProductList.as_view()),
    path('api/products/<int:id>/', views.ProductDetail.as_view()),
    # Users
    path('api/users', views.UserList.as_view()),
    path('api/users/<int:id>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)