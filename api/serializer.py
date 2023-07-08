from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ecommerce.models import Product

# serializers.HyperlinkedModelSerializer
# serializers.ModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['name']