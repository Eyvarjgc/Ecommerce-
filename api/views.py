from rest_framework import viewsets,permissions
from .serializer import ProductSerializer
from ecommerce.models import Product

class ViewProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

# class 