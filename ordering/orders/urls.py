from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='master'),
    path('water_order/', views.water_order, name='water_order'),
    path('list_order/', views.list_orders, name='list_orders'),
]