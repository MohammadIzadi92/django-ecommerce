from rest_framework import serializers
from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """
    Products serializer used for ProductsViewSets.
    """
    class Meta:
        model = Product
        fields = "__all__"
