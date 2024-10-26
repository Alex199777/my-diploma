from django.db import models

from django.contrib.auth.models import User

from goods.models import Product


# Create your models here.

class CartQueryset(models.QuerySet):
    '''Считает сумму всех товаров и количество'''

    def total_price(self):
        '''Итоговая сумма'''
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    name = models.CharField(max_length=255,default='Unknown')

    #Переопределяем manager.objects для возможности добавлять свои собственные методы
    objects = CartQueryset().as_manager()


    def product_price(self):
        '''Считает сумму с учетом количества товара'''

        return round(self.product.discount_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина - {self.user.username}; Товар - {self.product.name}; Количество - {self.quantity} '
        return f'Корзина - Аноним; Товар - {self.product.name}; Количество - {self.quantity} '