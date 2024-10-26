
from django.utils.http import urlencode

from goods.models import Category

from django import template

register = template.Library()

@register.simple_tag()
def tag_categories():
    '''Добавляем свой тег'''
    return Category.objects.all()

@register.simple_tag(takes_context=True)# Получаем все данные из нашего контекста
def change_params(context, **kwargs):

    #Создаем переменную , передаем context с ключом request и формируем словарь dict()
    query = context['request'].GET.dict()

    #Обновляем словарь с помощью метода update() другими именованнымми аргументами
    query.update(kwargs)
    return urlencode(query)# возвращает строку для формирования правильного url адреса


