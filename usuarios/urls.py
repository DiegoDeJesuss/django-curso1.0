from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro' ),
    path('clientes/', views.clientes, name = 'clientes' ),
]
