from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views




# DJANGO ADMIN RESET PASSWORD
# from django.contrib.auth import views as auth_views
# path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),



urlpatterns = [
    # USER PAGES
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('LogoutUser/',views.LogoutUser,name="LogoutUser"),
    # path('change_password', views.change_password,name="change_password"),
    # path('reset_password', views.reset_password,name="reset_password"),
    # path('reset/id/<token>',views.reset,name="reset"),


    # PAGES
    # path('carrito/', views.carrito,name='carrito'),
    path('carrito/<pk>', views.carrito,name='carrito'),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('genre/<pk>',views.genre,name='genre'),
    path('detail/<pk>',views.detail,name='detail'),
    path('updateamount', views.updateamount,name='updateamount'),
]
