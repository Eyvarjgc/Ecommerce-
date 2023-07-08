from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from ecommerce.models import Product
import json
from .serializers import ProductSerializers
from rest_framework.response import Response

# Create your views here.

# def Api2View(request):
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(data)
#     except:
#         pass
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)


@api_view(['GET'])
def Api2View(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['name', 'artist', 'get_price'])
        data = ProductSerializers(instance).data
    return Response(data)

@api_view(['POST'])
def Api2Add(request,*args, **kwargs):
    instance = ProductSerializers(data = request.data)
    if instance.is_valid():
        instance.save()
        data = instance.data
    return Response(data)