from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.good_index, name='good_search'),
    path('<slug:category_slug>/', views.good_index, name='good_index'),
    path('detail/<slug:good_slug>/', views.good_detail, name='good_detail')
]