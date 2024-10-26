from django import forms
from .models import Cart

class CartUpdateForm(forms.ModelForm):
    '''Форма для обновления количества товаров в корзине'''
    class Meta:
        model = Cart
        fields = ['quantity']
