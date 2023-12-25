# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.getHome, name='home'),
    path('foo-bar',views.getRouters, name='routes'),

]
