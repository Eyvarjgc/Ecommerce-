from django.urls import include,path
from .views import ViewProduct
from rest_framework import routers

router = routers.DefaultRouter()

# basename='porduct'

router.register(prefix='/products', viewset=ViewProduct,basename='/products')

urlpatterns = router.urls


# urlpatterns = [
#     path('product', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]