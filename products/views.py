from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product
from .serializers import ProductsSerializer

# Create your views here.


class ProductsViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
