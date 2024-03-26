from django.urls import path
from produit import views

urlpatterns = [
    path('create-produit/', views.CreateproduitView.as_view(), name='create-produit'),
    path('list-produit/', views.ListproduitView.as_view(), name='list-produit'),
]