from rest_framework import generics
from .models import Store, Product
from .serializers import StoreSerializer, ProductSerializer

class StoreListCreateView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        queryset = Store.objects.all()
        name = self.request.query_params.get('name', None)
        location = self.request.query_params.get('location', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

class StoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)
        manufacturer = self.request.query_params.get('manufacturer', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if manufacturer:
            queryset = queryset.filter(manufacturer__icontains=manufacturer)
        if category:
            queryset = queryset.filter(category__icontains=category)

        return queryset

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

