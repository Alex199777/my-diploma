from django.shortcuts import render

from goods.models import Category
from .models import CoverImage
from goods import models


# Create your views here.
def home(request):
    pictures = CoverImage.objects.all()
    context = {'pictures': pictures,

               }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')