from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('registration/', views.user_registration, name='user_registration'),
    path('profile/', views.user_profile, name='user_profile'),
    path('user-cart', views.user_cart, name='user_cart'),
    path('logout/', views.user_logout, name='user_logout'),

]