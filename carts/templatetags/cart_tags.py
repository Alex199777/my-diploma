from itertools import product

from carts.models import Cart

from django import template

register = template.Library()

@register.simple_tag()
def user_carts(request):
    '''Добавляем свой тег'''
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    else:
        return Cart.objects.filter(session_key=request.session.session_key)