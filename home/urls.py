
from django.urls import path
from . import views
from .views import about

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about')
]