
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


# Create your views here.

def create_order(request):

    #Если запрос post создаем форму
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                #Создаем пакет транзакций
                with transaction.atomic():
                    user = request.user
                    #Выбираем все корзины которые есть у пользователя
                    cart_items = Cart.objects.filter(user=user)

                    #Если Queryset содержит хотя бы один объект
                    if cart_items.exists():
                        #Формируем заказ по форме Order
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            pay=form.cleaned_data['pay'],
                        )
                        #Создаем заказаные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.name
                            price = cart_item.product.discount_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'{name}-нет такого количества на складе'
                                                      f'Доступное количество - {product.quantity}')

                            #Если прошли все проверки создаем на каждый товар заказ
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.save()

                        #Очистить корзину пользователя после заказа
                        cart_items.delete()
                        return redirect('user_profile')
            except Exception as e:
                print(f'Ошибка {e}')
                return redirect('user_cart')

    #Если запрос get создаем форму с предзаполненными данными с помощью параметра initial
    else:
        initial = {'username': request.user.username,
                   'last_name': request.user.last_name,}
        form = CreateOrderForm(initial=initial)
    context = {'form': form}
    return render(request, 'user_orders.html',context)