from rest_framework import serializers
from ecommerce.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'artist',
            'releasedate',
        ]