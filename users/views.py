from django.contrib import auth
from django.db.models import Prefetch
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.models import Order, OrderItem

from users.forms import UserLogin, UserRegistration, UserProfile


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')

    else:
        form = UserLogin()

    context = {'form': form}
    return render(request, 'user_login.html', context)





def user_registration(request):


    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():#Если форма валидна,сохраняем пользователя и перенаправляем на главную страницу
            form.save()
            return redirect('home')
    else:
        form = UserRegistration()

    context = {'form': form}
    return render(request,'user_registration.html', context)




def user_profile(request):

    if request.method == 'POST':
        form = UserProfile(data=request.POST, instance=request.user)#instance - позволяет работать с текущими данными пользователя
        if form.is_valid():#Если форма валидна,сохраняем изменение пользователя и перенаправляем обратно на страницу профиля
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfile(instance=request.user)
    orders = (Order.objects.filter(user=request.user)
              .prefetch_related(
        Prefetch("orderitem_set",
                 queryset=OrderItem.objects.select_related("product"),)
    ).order_by("-id"))

    context = {'form': form, 'orders':orders}
    return render(request,'user_profile.html', context)

def user_cart(request):
    return render(request, 'user_cart.html')


def user_logout(request):
    auth.logout(request)
    return redirect('home')
