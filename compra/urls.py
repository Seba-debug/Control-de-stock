from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
]
