from django.urls import path
from api2 import views

urlpatterns = [
    path('',views.Api2View),
    path('add',views.Api2Add),
]
