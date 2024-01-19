from django.urls import path
from .views import (
    StoreListCreateView, StoreRetrieveUpdateDestroyView,
    ProductListCreateView, ProductRetrieveUpdateDestroyView
)

urlpatterns = [
    path('stores/', StoreListCreateView.as_view(), name='store-list-create'),
    path('stores/<int:pk>/', StoreRetrieveUpdateDestroyView.as_view(), name='store-retrieve-update-destroy'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    
]
