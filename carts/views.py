from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST


from carts.forms import CartUpdateForm
from carts.models import Cart
from goods.models import Product


# Create your views here.

def cart_add(request, product_id):

    #Получаем экземпляр продукта по айдишнику
    product = Product.objects.get(id=product_id)

    # Если пользователь авторизован
    if request.user.is_authenticated:
        # Фильтруем корзину по продукту который юзер хочет добавить
        carts = Cart.objects.filter(user=request.user,product=product)

        #Если такой товар присутствует в корзине
        if carts.exists():
            #Присваиваем перменной первое значение из QuerySet
            cart = carts.first()
            cart.quantity += 1 #Увеличиваем количество товара
            cart.save()
        else:
            #Иначе создаем товар в корзине с количесвтом 1
            Cart.objects.create(user=request.user, product=product, quantity=1)

    # Если пользователь не авторизован
    else:
        if not request.session.session_key:
            request.session.create()
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)



    return redirect(request.META['HTTP_REFERER'])# Через ключ HTTP_REFERER атрибута META получаем возможность перезагрузить текущую страницу





@require_POST # Декоратор, который позволяет обрабатывать только POST запросы
def cart_change(request, product_id):
    # Получаем объект Cart для текущего пользователя и указанного продукта
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)
    else:
        cart_item = get_object_or_404(Cart, session_key=request.session.session_key,  product_id=product_id)
    # Получаем действие из POST-запроса (увеличить или уменьшить количество)
    action = request.POST.get('action')
    # Проверяем действие и обновляем количество товара в зависимости от него
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    # Сохраняем обновленные данные в базе
    cart_item.save()
    return redirect(request.META['HTTP_REFERER']) # Через ключ HTTP_REFERER атрибута META получаем возможность перезагрузить текущую страницу


def cart_remove(request, product_id):

    cart = Cart.objects.get(id=product_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])  # Через ключ HTTP_REFERER атрибута META получаем возможность перезагрузить текущую страницу