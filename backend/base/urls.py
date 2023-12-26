# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.getHome, name='home'),
    path('products/',views.getProducts, name='product-list'),
    path('products/<str:pk>/', views.ProductDetail, name='product-detail'),
    path('foo-bar',views.getRouters, name='routes'),

]
