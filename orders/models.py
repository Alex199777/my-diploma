
from django.contrib.auth.models import User
from django.db import models

from goods.models import Product


# Create your models here.
class OrderQueryset(models.QuerySet):

    def total_price(self):
        '''Итоговая сумма'''
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Пользователь', default=None )
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    pay = models.BooleanField(default=False, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=20, default='В пути', verbose_name='Статус заказа')

    def __str__(self):
        return f'Заказ {self.pk} -- Покупатель - {self.user.username} {self.user.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, null=True, verbose_name='Продукт', default=None)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    name = models.CharField(max_length=150, default='Unknown', verbose_name='Нaзвание',)
    objects = OrderQueryset.as_manager()
    def product_price(self):
        '''Считает сумму с учетом количества товара'''

        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f'Товар - {self.product.name}; Заказ - {self.order.pk}'
